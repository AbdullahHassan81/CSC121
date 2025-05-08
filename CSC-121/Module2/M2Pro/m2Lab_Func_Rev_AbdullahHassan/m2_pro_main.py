#import the module and assign alias 
import store_fun as fun

#Number of items
#Each item in the store cost $1
#Customers who buy 10 or more items are to get a 5% discount
#6.2% sales tax is applied on cost

#define the function
def subfun():
    return fun.store_fun() #function calls another and returns it 

#call the main function
def main():
    #nested function that prints a menu
    def menu():
        print("1) Calculate Cost")
        print("2) Exit")
        
    #call menu
    menu()
    
    #cost calculation 
    print("\nIMPORTANT How cost is calculated:\n")
    print("Each item in the store costs $1 dollar")
    print("Customer buying 10 or more items recieves 5% discount")
    print("Customer LESS than 10 items, recieves 0 discount")
    print("6.2% sales tax is applied")
    
    #initialize the user choices and loop it until user exits
    choice = 0
    while choice !=2:
        # Get user choice
        choice = int(input("\nEnter Choice: "))
   
   # Evaluate user choice
        if choice == 1:
       # Call the subfun function
           subfun()
        elif choice == 2:
               print("\nProgram Terminating....")
        else:
               print("Invalid Entry!!\n")
               # Call the menu again for invalid entry
               menu()
       
if __name__ == "__main__":
    main()