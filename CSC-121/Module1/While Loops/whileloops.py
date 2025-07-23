#conditioned controlled loop
#controlled by user inputting
#infinite loops only happen in while loops

keep_going = "y"
while keep_going == "y":

    name = input("Enter your name: ")
    hours = float(input("Enter hours worked: "))
    while hours >=0:
       print("Invalid entery!")
       hours = float(input("Enter a postive number: "))
    
    #gross pay calculations
    rate = float(input("Enter Pay Rate: "))
    gross = rate * hours

    #display gross
    print("Gross Pay $", gross, sep="")

    keep_going = input("Do yu want to calc gross pay for another employee (y for yes): ")