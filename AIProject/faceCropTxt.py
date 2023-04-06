import cv2
import os

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cwd = os.getcwd()
dirPath = "Pytorch_Retinaface/faceImg/JH"
cropDirPath = "Pytorch_Retinaface/faceCroped/croped_JH"

if not os.path.isdir(cropDirPath):
    os.mkdir(cropDirPath)
imgIdxList = os.listdir(dirPath)

# for imgIdx in imgIdxList:
#     imgIdxPath = os.path.join(dirPath, imgIdx)
#     imgRead = cv2.imread(imgIdxPath)
#     gray = cv2.cvtColor(imgRead, cv2.COLOR_BGR2GRAY)
#     detection = cascade.detectMultiScale(gray, 1.3, 5)

#     for (x, y, w, h) in detection:
#         imgRead = cv2.rectangle(imgRead, (x, y), (x + w, y + h), (255, 0, 0), 3)
#         # cropImg = imgRead[ y: y + h, x : x + w]
#         # print(cropImg)

#         # print(x1, y1, x2, y2)
#         # print(y, y + h, x, x + w)

#         imgRead = cv2.rectangle(imgRead, (x, y), (x + w, y + h), (255, 0, 0), 3)

#         cv2.imwrite(os.path.join(cropDirPath,imgIdx), imgRead)

        
# savedTruckImgNameList = os.listdir("plateTruck_images")
for imgIdxName in imgIdxList:
    src = os.path.join("plateTruck_images", imgIdxName) 
    txtName = imgIdxName.replace(".jpg", ".txt")
    print(txtName)
