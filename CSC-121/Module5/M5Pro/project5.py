#M5Pro
#3/31/25
#Abdullah Hassan
import stu_courses

# calling main function 
# displaying menu
def display_menu():
    """Display the menu to the user."""
    print('--------------------Menu--------------------')
    print("1 ) Select Courses, Course Grade and Calc Tuition")
    print("2 ) Calculate Tuition For Specific Students")
    print("3 ) Display Average and Total Tuition (All Students)")
    print("4 ) Display Student Info")
    print("5 ) EXIT")
    print('--------------------Menu--------------------')

def menu():
    #choice2 is calculating tuition for specific students 
        elif choice == 2:
            # Display list of students
            print("Select a student:")
            for i, name in enumerate(stu_names):
                print(f"{i+1}. {name}")
            student_index = int(input("Enter student number: ")) - 1
            tuition_cost = get_tuition_cost(student_index)
            print(f"Tuition cost for {stu_names[student_index]}: {tuition_cost:.2f}")
        #choice5 is exiting
        elif choice == EXIT:
            print("Exiting the program")
            break  # exit the loop

