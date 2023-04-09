import os, random, shutil

imgFolderNamePath = "Pytorch_Retinaface/faceImg/SB"
valImgFolderNamePath = "Pytorch_Retinaface/faceImg/SB_val"
labelFolderNamePath = "Pytorch_Retinaface/faceLabelCroped/labelCroped_SB"
valLabelFolderNamePath = "Pytorch_Retinaface/faceLabelCroped/labelCroped_SB_val"

if not os.path.isdir(valImgFolderNamePath):
    os.mkdir(valImgFolderNamePath)
if not os.path.isdir(valLabelFolderNamePath):
    os.mkdir(valLabelFolderNamePath)

imageNameList = os.listdir(imgFolderNamePath)

sampleImgNameList = random.sample(imageNameList, int(len(imageNameList) * 0.2))
for sampleImgName in sampleImgNameList:
    valImgPath = os.path.join(imgFolderNamePath, sampleImgName)
    shutil.move(valImgPath, valImgFolderNamePath)

    valLabelName = sampleImgName.split(".")[0] + ".txt"
    valLabelPath = os.path.join(labelFolderNamePath, valLabelName)
    shutil.move(valLabelPath, valLabelFolderNamePath)