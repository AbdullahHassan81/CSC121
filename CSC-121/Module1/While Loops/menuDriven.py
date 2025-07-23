#menu driven program (displays menu)

choice = 0 #assign it value thats not used
while choice != 2:

    print("----------Menu----------")
    print("1) To Calculate Gross Pay")
    print("2) To Exit")

    print("-------------------------\n")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter Employee Name: ")
        hours = float(input("Hours Worked: "))
        rate = float(input("Enter Pay Rate: "))
        gross = rate * hours

        print("Gross pay $", gross, sep="")
    elif choice ==2:
        print("Program Ended\n")

    else:
        print("Invalid Entry")