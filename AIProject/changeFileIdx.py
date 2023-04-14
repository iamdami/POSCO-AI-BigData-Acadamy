import os
import os.path
import glob

dirPath = "4face/4face_JH_label_val/"
fileName = "*.txt"
labelFileList = glob.glob(dirPath + fileName)

for labelFile in labelFileList:
    with open(labelFile, "r") as f:
        data = f.read()
    data = data.replace("0 ", "3 ")
    print(labelFile)
    print(data)

    with open(labelFile, "w") as f:
        f.write(data)
