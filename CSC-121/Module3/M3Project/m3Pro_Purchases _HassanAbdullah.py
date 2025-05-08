#This program calculates tuition cost for students depending on their course
#3/3/25
#CSC-121 m3Pro - Purchases
#Abdullah Hassan

#student names
stu_names = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]

#courses
courses = ["MAT 035(Concepts of Algebra)", "CTI 115(Computer System Foundations)", "BAS 120 Intro to Analytics", "CSC 121 Python Programming"]

#tuition costs
tuition = [460, 520.98, 500, 783.88]

#calls the main function
def main():
    course_display([stu_names, tuition]) #trying to pass courses and tuition in a tabular format 
    
def menu():
    #choice variable 
    choice = 0
    
    while choice != EXIT:
        #menu displayed
        display_menu()
    
        choice = int(input("Enter your choice: "))
    
        if choice ==1 :
            print(f'{[stu_names]<:10}{[tuition]<:10}')
        
        elif choice==2 :
            print(f'{[stu_names]<:10}{[tuition]<:10}')
            
        elif choice ==3:
            print("Exitng the program")
            
        else:
            print("Error: Invalid Entry")

def display_menu():
    print('----------Menu----------')#thisneeds to be after the course name and tuition
    print("1 )Calculate Tuition For All Students")
    print("2 )Calculate Tuition For Specific Students")
    print("3 )EXIT")
        
