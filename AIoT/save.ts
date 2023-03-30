import { Mutex } from 'async-mutex';
import http from 'http';
import { JSONFile, Low } from 'lowdb'; // eslint-disable-line import/no-unresolved
import moment from 'moment';
import path from 'path';
import pino from 'pino';
import { fileURLToPath } from 'url';

const log = pino();

type DBObject = {[key: string]: FixedLengthArray<number, 2>[];}
const dbFilePath = path.join(path.dirname(fileURLToPath(import.meta.url)), '..', '..', 'db.json');
const lowAdaptor = new JSONFile<DBObject>(dbFilePath);
const db = new Low<DBObject>(lowAdaptor);
const dbMutex = new Mutex();
let isDBReady = false;

const saveData = async (I: http.IncomingMessage, O: http.OutgoingMessage) => {
  const doResponse = (code: number = 0, message: string = 'Save sucessful') : object => {
    let realMessage = message;
    if (code === 0) realMessage = 'Save successful';
    const returnObject = {
      code,
      message: realMessage,
    };
    O.setHeader('Content-Type', 'application/json; charset=utf-8');
    O.end(JSON.stringify(returnObject));
    return returnObject;
  };

  if (I.method !== 'POST') {
    log.info(doResponse(1, 'Method not allowed'));
    return;
  }

  // @ts-ignore
  if (I.body === null) {
    log.info(doResponse(1, 'No data provided'));
    return;
  }

  const dbMutexRelease1 = await dbMutex.acquire();
  try {
    if (!isDBReady) {
      await db.read();
      isDBReady = true;
      log.info(`DB is ready, on : ${dbFilePath}`);
    }
  } finally {
    dbMutexRelease1();
  }

  // @ts-ignore
  const receivedData = I.body
    .split('\n')
    .map((line: string) => {
      if (line.includes('=')) {
        return { k: line.split('=')[0], v: line.split('=')[1] };
      }
      return null;
    }).filter(Boolean);

  const putDataInObject = (obj: object) => ({
    ...obj,
    receivedData,
  });

  const dbMutexRelease2 = await dbMutex.acquire();
  const data = db.data || {};
  receivedData.forEach((obj: { [key: string]: string; }) => {
    const { k, v } = obj;

    const vTime: FixedLengthArray<number, 2> = [moment().valueOf(), Number.parseFloat(v)];
    if (Number.isNaN(vTime[1])) {
      log.info(doResponse(2, `Invalid value for ${k} : ${v}`));
      dbMutexRelease2();
      return;
    }

    if (k in data) {
      data[k].push(vTime);
    } else {
      data[k] = [vTime];
    }
  });
  db.data = data;
  let isSavesuccessful = false;
  while (!isSavesuccessful) {
    try {
      // eslint-disable-next-line no-await-in-loop
      await db.write();
      isSavesuccessful = true;
      dbMutexRelease2();
      log.info(putDataInObject(doResponse()));
    } catch (e) {
      log.error(e);
    }
  }
};

export default saveData;
