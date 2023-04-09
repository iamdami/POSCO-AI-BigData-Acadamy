import os
imgPath = "Pytorch_Retinaface/faceImg/train"
labelpath = "Pytorch_Retinaface/faceLabelCroped/train"
imgList = os.listdir(imgPath)
labelList = os.listdir(labelpath)
print(len(imgList))
print(len(labelList))

delNameList = []
if len(labelList) < len(imgList):
    for imgName in imgList:
        delNameList.append(imgName.split('.')[0])
    for labelName in labelList:
        if labelName.split('.')[0] in delNameList:
            delNameList.remove(labelName.split('.')[0])
    print(f"1: {delNameList}")
elif len(labelList) > len(imgList):
    for labelName in labelList:
        delNameList.append(labelName.split('.')[0])
    for imgName in imgList:
        if imgName.split('.')[0] in delNameList:
            delNameList.remove(imgName.split('.')[0])
    print(f"2: {delNameList}")
else:
    print("Equal")
    exit()
    
for delName in delNameList:
    delName = f"{delName}.jpg"
    os.system(f"rm -rf {os.path.join(imgPath,delName)}")

print(f"after: {len(os.listdir(imgPath))}")
print(f"after: {len(os.listdir(labelpath))}")
