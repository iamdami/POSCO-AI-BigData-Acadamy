import sys

# print(sys.argv)
fr = open(sys.argv, "r")
fw = open(sys.argv, "w")
for line in fr:
    fw.write(line)
fr.close()
fw.close()
