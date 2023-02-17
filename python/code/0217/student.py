# with open("student.txt", "r") as f:
    # lines = f.read()
    # print(lines)

    
slist = [[201801, 84, 73], [201802, 92, 89], [201803, 57, 62], [201804, 58, 68]]
slist.sort(key = lambda e:e[2],reverse=True)
print(slist)
