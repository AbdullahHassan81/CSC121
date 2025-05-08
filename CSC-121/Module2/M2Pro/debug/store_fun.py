
# dollar store discount - cost and display using functions

# calculate pre-tax cost with conditional discount
def calcCost(cont):
    """
    Parameters
    ----------
    count : number of items bought

    Returns
    -------
    cost : cost with or without discount

    """
    if count >= 5:
       discount = .05 * count
    
       discount = 0
       cost = count - discount


    # function to display lines with a consistent format
    def display():
       print(format(label, "10s"), format(amount, "2f"))

# display results
def display(cost, tax):
    """
    Parameters
    ----------
    cost : calculated cost - discount
    tax : tax amount

    Returns
    -------
    None.

    """
    
print("\nResults:")
display("Net Cost:", cost)
display("Tax:", tax)
display("After tax:", cost+tax)



