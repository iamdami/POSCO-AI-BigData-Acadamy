import cv2
import os

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

oriFaceImgDir = "Pytorch_Retinaface/faceImg/DS"
txtDir = "Pytorch_Retinaface/faceLabelCroped/labelCroped_DS"

if not os.path.isdir(txtDir):
    os.mkdir(txtDir)

for f in os.listdir(oriFaceImgDir):
    if f.endswith('.jpg'):
        img_name = os.path.splitext(f)[0]
        txt_name = img_name + '.txt'
        img_path = os.path.join(oriFaceImgDir, f)
        txt_path = os.path.join(txtDir, txt_name)

        imgRead = cv2.imread(img_path)
        gray = cv2.cvtColor(imgRead, cv2.COLOR_BGR2GRAY)
        detection = cascade.detectMultiScale(gray, 1.3, 5)

        with open(txt_path, 'w') as file:
            for (x, y, w, h) in detection:
                centerX = x + w/2
                centerY = y + h/2

                imgWidth, imgHeight = imgRead.shape[1], imgRead.shape[0]
                centerX /= imgWidth
                centerY /= imgHeight

                bboxWidth = w / imgWidth
                bboxHeight = h / imgHeight

                yoloBboxStr = f"{centerX:.6f} {centerY:.6f} {bboxWidth:.6f} {bboxHeight:.6f}"
                file.write(yoloBboxStr + '\n')
