students = {}

while True:
    print("1 Add Student")
    print("2 View Students")
    print("3 Exit")

    choice = input()

    if choice == "1":
        name = input("Name: ")
        students[name] = True

    elif choice == "2":
        print(students)

    elif choice == "3":
        break
