import csv # import csv
from menu import display_menu #import the modularized menu

'''

Identify and fix the errors in the script.

Ensure the program correctly classifies order amounts into
"Small Order," "Medium Order," and "Large Order."
'''
READ_CHOICE = 1
ADD_CHOICE = 2
EXIT_CHOICE = 3

 

def process_orders(filename):

    choice = 0
    while choice != EXIT_CHOICE:
        display_menu()
        choice = int(input('Enter your choice: ')) # asks user to enter choice
    
        if choice == READ_CHOICE: 
    
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header 
                order_summary = ""
                
                for row in reader:
                    customer_name = row[0]
                    order_amount = float(row[1])
                    
                    if order_amount < 50:
                        category = "Small Order"
                    elif order_amount >= 50 and order_amount < 200:
                        category = "Medium Order"
                    elif order_amount >= 200:
                        category = "Large Order"
                    
                    order_summary += f"{customer_name} - {category}\n"
                    
                with open("summary.txt", "w") as summary_file:
                    summary_file.write(order_summary)
                    print("Summary successfully written.")
        
        elif choice == ADD_CHOICE:
            
                name = input('Customer Name: ') # asks for customer name
                amount = int(input('Amount: ')) # asks for amount
    
                # puts all of the user's input into a list.
                newentry = [name, amount]
    
                filename = 'orders.csv'
    
                with open(filename, 'a', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter. writerow(newentry) # writes the new entry
        
        elif choice == EXIT_CHOICE:
            print('Exiting the program.......') # ends program
        else: # displays error if anything other than choices is entered.
            print()
            print('Error: invalid entry')
            print('Try again')


process_orders("orders.csv")
