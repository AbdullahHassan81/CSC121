import circle
import rectangle
# Constants for the menu choices

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_REC_CHOICE = 4
QUIT_CHOICE = 5

# The main function

def main():

    # The choice variable controls the loop
    # and hold the user's menu choice

    choice = 0

    while choice != QUIT_CHOICE:

        # display menu
        display_menu()

        # get user's choice
        choice = int(input("Enter your choice: "))

        # Perform the calculation selected
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print("The area is", format(circle.area(radius),'.2f'))

        elif choice == CIRCUMFERENCE_CHOICE:
            
            radius = float(input("Enter the circle's radius: "))
            print("The circumference is", circle.circumference(radius))
        
        elif choice == AREA_RECTANGLE_CHOICE:
            
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's lenght: "))
            print("The area is", rectangle.area(width,length ))

        elif choice == PERIMETER_REC_CHOICE:
            
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's lenght: "))
            print("The parimeter is", rectangle.perimeter(width,length ))
        elif choice == QUIT_CHOICE:
            print("Exiting the program.......")

        else:
            print("Error: invalid entry")

    # display menu options
def display_menu():

    print(' MENU')
    print("1)  Area of a circle")
    print("2)  Circumference of a circle")
    print("3)  Area of a rectangle")
    print("4)  Parimeter of a rectangle")
    print("5)  Quit")

if __name__ =="__main__":
    main()










