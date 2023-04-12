import os
import os.path
import glob

dirPath = "Pytorch_Retinaface/faceLabelCroped/labelCroped_JK"
fileName = "/*.txt"
inputNum = input("your file Num : ")
print(inputNum.isdigit())
labelFileList = glob.glob(dirPath + fileName)
print(len(labelFileList))
if inputNum.isdigit() and len(labelFileList) == int(inputNum):
    for labelFile in labelFileList:
        with open(labelFile, "r") as f:
            lines = f.readlines()
        with open(labelFile, "w") as f:
            for line in lines:
                f.write('4 ' + line)
else:
    print(f"your file Num : {len(labelFileList)}")
    print("or your input type not int")
