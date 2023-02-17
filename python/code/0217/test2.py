import os

filename = input("enter a file name: ")
f = open(filename, "r")
if not os.path.exists(filename):
    print("error")
else:
    for i in filename:
        line = f.readline()
        print(line.upper(), end=" ")
f.close()