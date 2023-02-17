# f = open("new1.txt", "w")

# for i in range(1, 6):
#     data = "%d line\n" % i
#     f.write(data)

# f.close()

f = open("new1.txt", "r")
line = f.readline()
print(line, end='')
line = f.readline()
print(line, end='')
f.close()