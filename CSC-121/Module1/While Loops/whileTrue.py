#what not to do
while True: 
    name = input("Enter employee name or stop: ")

    if name == "stop":

        break
    else: 
        hours = float(input("Enter hours worked: "))
        while hours <0: 
            print("Invalid Entry")
            hours = float(input("Enter positive hours: "))

        rate = float(input("Enter pay rate: "))
        gross = rate * hours
        print("Gross Pay $", gross, sep="")

