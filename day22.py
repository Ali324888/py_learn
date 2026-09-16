# with open("student.txt","w") as file:
#     file.write("Name: Zee\n")
#     file.write("Age: 30\n")
#     file.write("City: Delhi")

# print("Notes added successfully!")

# with open("student.txt", "r") as file:
#     notes = file.read()
#     print(notes)

# name = input("Enter name: ")
# age = input("Enter age: ")
# city = input("Enter city: ")

# with open("student2.txt", "w") as file:
#     file.write(name)
#     file.write(age)
#     file.write(city)

# print("Notes Added")


# choice = input("Enter choice [1,2]: ")

# if choice == "1":
#     notes = input("Enter Your Note: ")
#     with open("notes.txt", "a") as file:
#         file.write(notes+"\n")

# elif choice == "2":
#     with open("notes.txt", "r") as file:
#         notes = file.read()
#         print(notes)
# else: 
#     print("Invalid Choice!")


while True:

    print("\n1. Add note")
    print("2. Read note")
    print("3. Clear notes")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        note = input("Enter Your Note: ")
        with open("notes.txt", "a") as file:
            file.write(note+"\n")
            print("Note added successfully!")
    elif choice == "2":
        with open("notes.txt", "r") as file:
            note = file.read()
            if note == "":
                print("No notes found!")
            else:
                print("\nYour Notes:")
                print(note)
    elif choice == "3":
        with open("notes.txt", "w") as file:
            file.write("")
            print("Notes cleared!")
    elif choice == "4":
        print("Exit")
        break
    else:
        print("Invalid Choice!")
