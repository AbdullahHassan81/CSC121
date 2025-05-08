#student names
stu_names = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]

#courses
courses = ["MAT 035(Concepts of Algebra)", "CTI 115(Computer System Foundations)", "BAS 120 Intro to Analytics", "CSC 121 Python Programming"]

#tuition
course_tuition = [460, 520.98, 500, 783.88]
EXIT = 3  

# calling main function 
# displaying menu
def display_menu():
    """Display the menu to the user."""
    print('--------------------Menu--------------------')
    print("1 ) Calculate Tuition For All Students")
    print("2 ) Calculate Tuition For Specific Students")
    print("3 ) EXIT")
    print('--------------------Menu--------------------')

#getting the tuition costs
def get_tuition_cost(student_index):
    """Get tuition cost for a student."""
    tuition_cost = 0
    for i, course in enumerate(courses):
        confirm = input(f"Is {stu_names[student_index]} registered in {course}? (y/n): ")
        if confirm.lower() == 'y':
            # Correctly index the course_tuition list
            tuition_cost += course_tuition[i]
    return tuition_cost

#menu function
def menu():
    """Main menu loop."""
    for _ in range(100):  # loop 100 times
        display_menu()
        choice = int(input("Enter your choice: "))
        #choice1 is calculating tuition for all students
        if choice == 1:
            print(f"{'Student Name':<20}{'Tuition Cost':<10}")
            for i in range(len(stu_names)):
                tuition_cost = get_tuition_cost(i)
                print(f"{stu_names[i]:<20}{tuition_cost:<10.2f}")
                #print("Enter y for yes: ")

        #choice2 is calculating tuition for selected students 
        elif choice == 2:
            # Display list of students
            print("Select a student:")
            for i, name in enumerate(stu_names):
                print(f"{i+1}. {name}")
            student_index = int(input("Enter student number: ")) - 1
            tuition_cost = get_tuition_cost(student_index)
            print(f"Tuition cost for {stu_names[student_index]}: {tuition_cost:.2f}")
        #exiting the program choice 
        elif choice == EXIT:
            print("Exiting the program")
            break  # exit the loop

#calling the main functions
def main():
    """Call the main function."""
    menu()

main()
