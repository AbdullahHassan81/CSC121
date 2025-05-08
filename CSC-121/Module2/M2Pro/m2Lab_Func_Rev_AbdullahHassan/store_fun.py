# dollar store discount - cost and display using functions

# calculate pre-tax cost with conditional discount
def calcCost(count):
    """
    Parameters
    ----------
    count : number of items bought

    Returns
    -------
    cost : cost with or without discount

    """
    #check if the # of items qualify for a discount
    if count == 10:
       discount = 0.05 * count
    else:
       discount = 0
       
    #calculating cost
    cost = count - discount
    return cost 

    # function to display lines with a consistent format
def display(label, amount):
    print(f"{label :10s} {amount :2f}")

# calculate tax 
def calcTax(cost, tax_rate):
    """
    Parameters
    ----------
    cost : calculated cost - discount
    tax : tax amount

    Returns
    -------
    None.

    """
#getting user input as well as setting a few calculations
count = int(input("How many items did you buy?"))
tax_rate = 0.068
cost = calcCost(count)
tax = cost * tax_rate


#display results    
print("\nResults:")
display("Net Cost:", cost)
display("Tax:", tax)
display("After tax:", cost+tax)