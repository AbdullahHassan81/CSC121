# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 15:54:12 2025

@author: someb
"""
from run import courses, students 
#used python tutor 

#EXIT option 
EXIT = 6
#MENU
def menu():
    """Display the menu to the user."""
print("----------MENU----------")
print("1) Display Course Information") 
print("2) Lookup Course") 
print("3) Display Courses and Tuition for Specific Students") 
print("4) Display Tuition for All Students")
print("5) Display # of Students and Tuition for All Courses") 
print("6) EXIT") 
print("------------------------")


#menu function
def course():
    # Get the course from the user
 course = input("What course are you looking for? ")

 # Define the valid courses with tuition
 valid_courses = [
     {"code": "MAT-035", "tuition": 460},
     {"code": "CTI-115", "tuition": 520.98},
     {"code": "BAS-120", "tuition": 500},
     {"code": "CSC-121", "tuition": 783.88}
 ]

 # Check if the course is valid
 for c in valid_courses:
     if course == c["code"]:
         print(f"{course} is a valid course with tuition: ${c['tuition']:.2f}")
         return  # stop searching after finding the course
 print("Try again")
     
#for option 2 
def course_lookup():
    # Get the course from the user
    course_code = input("What course are you looking for? ")

    # Check if the course is valid
    if course_code in courses_dict:
        print(f"{course_code} is a valid course:")
        print(f"Description: {courses_dict[course_code]['desc']}")
        print(f"Tuition: ${courses_dict[course_code]['tuition']:.2f}")
    else:
        print("Try again")
        
#calling the main functions
def main():
    """
    Returns
    -------
    None.
    """
main()

#while loop 
#choice variable 
choice = 0
 
while choice != EXIT:
 
    choice = int(input("Enter your choice: "))
 
    #gives the course options
    if choice ==1:
        for course_code, course_info in courses.items():
            print(f"{course_code:<10}{course_info['desc']:<20}{course_info['tuition']:>10}")    
            #course_lookup()   
     
    #looksup courses 
    elif choice==2:
        course()
         
    #displays info for specifc students     
    elif choice ==3:
        student_list = list(students.keys())
        print("Select a student:")
        for i, name in enumerate(student_list):
            print(f"{i+1}. {name}")
        student_index = int(input("Enter student number: ")) - 1
        selected_student = student_list[student_index]
        courses_taken = students[selected_student]
        print(f"{selected_student}'s Courses and Tuition:")
        for course_code in courses_taken:
            print(f"{course_code}  {courses[course_code]['desc']}   ${courses[course_code]['tuition']:,.2f}")
        tuition_cost = sum([courses[course_code]['tuition'] for course_code in courses_taken])
        print(f"Overall Total ${tuition_cost:,.2f}")

    #displays tuition for all students 
    elif choice ==4:
        #Initialize a dictionary to store course enrollment
        course_enrollment = {course: 0 for course in courses.keys()}
        
        # Initialize a list to store student tuition information
        student_tuitions = [] 
        
        # Iterate over each student and their courses
        for student, courses_taken in students.items():
            tuition_cost = 0  # Initialize tuition cost for each student
            
            # Iterate over each course taken by the student
            for course in courses_taken:
                course_enrollment[course] += 1  # Increment course enrollment
                tuition_cost += courses[course]['tuition']  # Add course tuition to student's tuition
                
            # Append student's tuition information to the list
            student_tuitions.append({"Student": student, "Number of Courses": len(courses_taken), "Total Tuition": tuition_cost})
        
        # Calculate the total tuition for all students
        total_tuition = sum([s["Total Tuition"] for s in student_tuitions])
        
        # Print student tuition information
        print(f"{'Student':<20}{'Number of Courses':<20}{'Total Tuition':<20}")
        for s in student_tuitions:
            print(f"{s['Student']:<20}{s['Number of Courses']:<20}{s['Total Tuition']:<20}")
        
        # Print total tuition
        print(f"{'Total':<20}{'':<20}{total_tuition:.2f}")
        
    elif choice ==5:

        #Initialize dictionaries to store course counts and total tuitions
        course_counts = {}
        course_tuitions = {}

        #Iterate over the students and their courses
        for student, courses_taken in students.items():
            for course in courses_taken:
            #Count the number of students in each course
                if course in course_counts:
                    course_counts[course] += 1
                else:
                    course_counts[course] = 1

        #Calculate the total tuition for each course
        for course, count in course_counts.items():
            #Get the tuition for the current course
            tuition = courses[course]["tuition"]
            #Calculate the total tuition
            total_tuition = tuition * count
            course_tuitions[course] = total_tuition

        #Print the results
        print(f"{'Course':<10}{'Number of Students':<20}{'Total Tuition':<15}")
        for course, count in course_counts.items():
            tuition = course_tuitions[course]
            print(f"{course:<10}{count:<20}{tuition:.2f}")

    elif choice ==EXIT:
        print("Exiting, Goodbye")