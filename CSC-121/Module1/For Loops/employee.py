#for loop part 1
#ask for employee name
name = input("Enter name: ")

#getting rates and hours 
rate = float(input("Pay Rate: "))
hours = float(input("Hours Worked: "))

#calculating gross pay
gross = rate * hours

#displaying gross
print(f"Gross Pay ${gross}")
#this one ends 

#calculating running total every loop
total = 0
#fixed loop and count controlled
for name in ["Muhammad", "Yahya", "Yousef"]:
    #ask for employee name
    print("Enter info for", name)

    #getting rates and hours 
    rate = float(input("Pay Rate: "))
    hours = float(input("Hours Worked: "))

    #calculating gross pay
    gross = rate * hours
    total += hours 
    #displaying gross
    print(f"Gross Pay ${gross}")
#this one ends 

#run a range function for 5 employees
#calculating running total every loop
total = 0
#fixed loop and count controlled
for var in range(5): #the loop goes up to 5 not to 5 (ends at 4)
#for var in range(1,5) means it starts at 1 and ends at 4
    #ask for employee name
    print("Enter info for employee", var)

    #getting rates and hours 
    rate = float(input("Pay Rate: "))
    hours = float(input("Hours Worked: "))

    #calculating gross pay
    gross = rate * hours
    total += hours 
    #displaying gross
    print(f"Gross Pay ${gross}")

    print("\nTotal amounts to be paid $", total, sep="")



 
