def show_fun():
    print("show!")

def add_fun():
    print("add!")

while True:
    command = input("# ")
    if command == "show":
        show_fun()
    elif command == "add":
        add_fun()
    elif command == "quit":
        break
    else:
        print("wrong!")
