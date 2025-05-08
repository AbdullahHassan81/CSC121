#1/15/25
#example program
#get the bill amount n tip percentage

bill = float(input("Enter bill amount $"))
tipPer = float(input("Enter tip percentage (15%, 20% or 25%): "))
# evaluate tip
#removed decimal points
#if you use a decimal than the program wont work (use whole numbers)

if tipPer == 15:
    tipPer = 0.15
elif tipPer ==20:

    tipPer = 0.2

elif tipPer ==25:
    tipPer = 0.25
elif tipPer <15:
    tipPer=0.20
    print("Tip entered is below 15%!! therefore 20% tip applied")
else: #thank the person
    print("Thanks for the tip!")
    tipPer = tipPer/100
    
#calculate tip and total

tip = bill * tipPer

total = bill + tip
#show result
print("Total to be paid $", total, sep='')
#to round it do: print("Total to be paid $", round(total,2), sep='')
