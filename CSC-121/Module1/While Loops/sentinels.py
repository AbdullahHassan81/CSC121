#sentinels (its a value you have that stops the program)

name = input("Enter Employee name or Stop: ") #the stop is the sentinel
while name != "Stop":
    hours = float(input("Enter Hours Worked: "))
    while hours <0: 
        print("Invalid Entry")
        hours = float(input("ENter hour worked again: "))

    #calculate gross pay
    rate = float(input("Enter pay rate: "))
    gross = rate * hours

    #calculate gross
    print("Gross pay $", gross, sep="")
    name = input("Enter Employee name or Stop: ") #the stop is the sentinel


