global stuValue
stuValue = "%-15s %-20s %-10d %-10d %-10s %-10s"

stuDict = {}

def callMenu():
    print("%-15s %-18s %-11s %-9s %-10s %-10s" % ("Student", "Name", "Midterm", "Final", "Average", "Grade"))
    print("-" * 75)

def average(a, b):
    return (a + b) / 2 

def Grade(avg) :
    if avg >= 90:
        return 'A'
    elif avg >= 80 :
        return 'B'
    elif avg >= 70 :
        return 'C'
    elif avg >= 60 :
        return 'D'
    else:
        return 'F'

def show(a) : 
    callMenu()
    sortedAll = sorted(stuDict.items(), key = lambda a : a[1][4], reverse = True)
    for stu in sortedAll :
        print("%-15s %-20s %-10d %-10d %-10s %-10s" % (stu[1][0], stu[1][1], stu[1][2] , stu[1][3] ,stu[1][4], stu[1][5])) 

def search(a) :
    global stuValue
    stuNum = input("Student ID: ")
    for i in a :
        if i == stuNum :
            callMenu()
            print(stuValue % (a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
            return
    print("NO SUCH PERSON")

def changescore(a) :
    global stuValue
    stuNum = input("Student ID: ")
    for i in a :
        if i == stuNum :
            midOrFinal = input("Mid/Final? ").lower()
            if midOrFinal == "mid" :
                newScore = int(input("Input new score: "))
                if 0 > newScore or newScore > 100 :
                    return
                callMenu()
                print(stuValue % (a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
                print("Score changed.")
                a[i][2] = newScore
            elif midOrFinal == "final" :
                newScore = int(input("Input new score: "))
                if 0 > newScore or newScore > 100:
                    return
                callMenu()
                print(stuValue % (a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
                print("Score changed.")
                a[i][3] = newScore
            else :
                return
            a[i][4] = average(a[i][2],a[i][3])
            a[i][5] = Grade(a[i][4])
            print(stuValue % (a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
            return
    print("NO SUCH PERSON")

def searchgrade(a) :
    global stuValue
    grade = input("Grade to search: ").upper()
    if grade not in ['A', 'B', 'C', 'D', 'F'] :
        return
    flag = False
    for i in a :
        if a[i][5] == grade :
            print(stuValue % (a[i][0],  a[i][1], a[i][2] , a[i][3] ,a[i][4], a[i][5]))
            flag = True
    if not flag :
        print('NO RESULTS')

def add (a) :
    stuNum = input("Student ID: ")
    for i in a :
        if i == stuNum :
            print('ALREADY EXISTS')
            return
    name = input('Name : ')
    mid = int(input('Midterm Score : '))
    if 0 > mid or mid > 100 :
        return
    fin = int(input('Final Score : '))
    if 0 > fin or fin > 100 :
        return
    avg = average(mid,fin)
    stuDict[stuNum] = [stuNum, name, mid ,fin ,avg ,Grade(avg)]
    print('Student added.')

def remove(a) :
    if len(a) == 0 :
        print('List is empty')
        return
    stuNum = input("Student ID: ")
    for i in range(len(a)) :
        if stuNum in a:
            a.pop(stuNum)
            print('Student removed.')
            return
    print('NO SUCH PERSON')

def quit(a) :
        filename = input('Filename : ')
        fWrite = open(filename, "w")
        for i in a :
            s = '%s\t %s\t %d\t %d\n' % (a[i][0], a[i][1], a[i][2], a[i][3])
            fWrite.write(s)
        fWrite.close()

def main() :
    f = open("students.txt", "r")
    for x in f:
        stuDict[x.split()[0]] = [x.split()[0], x.split()[1] + " " + x.split()[2], int(x.split()[3]), int(x.split()[4]),
                                  (average(int(x.split()[3]), int(x.split()[4]))),
                                  Grade((average(int(x.split()[3]), int(x.split()[4]))))]
    f.close()

    show(stuDict)
    while True :
        command = input('# ').lower()
        if command == "show" :
            show(stuDict)
        elif command == "search" :
            search(stuDict)
        elif command == "changescore" :
            changescore(stuDict)
        elif command == "add" :
            add(stuDict)
        elif command == "searchgrade" :
            searchgrade(stuDict)
        elif command == "remove" :
            remove(stuDict)
        elif command == "quit" :
            save = input("Save data? [yes/no]").lower()
            if save == "yes" :
                quit(stuDict)
                break
            elif save == "no":
                break
            else:
                pass

if __name__ == "__main__":
    main()