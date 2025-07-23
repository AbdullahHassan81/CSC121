#Nested Loops
#hrs mins secs
'''
for hour in range(24):

    for mins in range(60):

        for secs in range(60):
            
            print(f'{hour}{mins}{secs}')
'''
#nested loop
rate = 30 
total = 0
for var in range(1, 4):

    for value in ["name", "hours worked"]:

        if value == "name":
            name = input("Enter employee " + value +": ")
        else:
            hours = float(input("Enter " + value + ": "))
            gross = hours * rate 
            total = total + gross

            print("Gross pay $", gross,sep = "")
print("\nTotal amounts to be paid $", total, sep="")