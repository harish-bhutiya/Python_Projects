def menu():
    print("1- Option 1: Convert string to uppercase")
    print("2- Option 2: convert string to lowercase")
    print("3- Option 3: slice the string a start index to an end index")
    print("4- Option 4: calculate the length od the string")
    print("5- Option 5: Loop through each character in the string and display it on a new line")


char = (input("Please enter your idea: "))
print(char)
menu()

option = int(input("Please enter your option: "))

while char != 0:
    if option == 1:
        print(char.upper())
    elif option == 2:
        print(char.lower())
    elif option == 3:
     slice_char= char[0:]
     print(slice_char)
    elif option == 4:
       print(len(char))
    elif option == 5:
       for char in char:
        print(char)

    else:
     print("Select valid option")

    print()
    menu()
    option = int(input("Please enter your option: "))

print("Thank yo for using our service")
