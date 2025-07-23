try:
    num1 = int(input("Enter Num: "))

    num2 = int(input("ENter another Num: "))

except ValueError:
    print("Invalid Entry")
    print("Whole # Should be Entered")

except:
    print("An error occured")

else:
    total = num1 + num2 
    print(total)