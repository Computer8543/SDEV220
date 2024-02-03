""" Name: Kyle Ingersoll

    File Name: M02_Lab_Case_Study_if_else_and_while.py
    
    Description: My app will prompt the user for a student's last and first 
    name. If the last name entered is "ZZZ" then the program ends.
    Then the user is prompted for their GPA as a float number. If the GPA is
    3.25 or greater, then the student made the Honor Roll.
    If GPA is 3.5 or greater, than the student made the Dean's List.
    
    List and description of variables: 
        student_last_name: stores student's last name as a string
        student_first_name: stores student's first name as a string
        student_GPA: stores student's GPA as a float 
        
    
"""
# variables for the student's data
student_last_name: str = ""
student_first_name: str = ""
student_GPA: float = 0.0

while student_last_name != 'ZZZ':
    # Prompt for and input student's first name, last name, and GPA
    # If student's last name is equal to ZZZ, then end the loop
    student_last_name = input("Enter student's last name:")
    if student_last_name == 'ZZZ':
        break
    student_first_name = input("Enter student's first name:")
    student_GPA = float(input("Enter student's GPA:"))
    
    # Check student GPA to see if student made either/or the Honor Roll or the Dean's List
    if student_GPA >= 3.5:
        print(student_first_name, student_last_name, "made the Dean's List.")
        print(student_first_name, student_last_name, "made the Honor Roll.")
    elif 3.5 > student_GPA >= 3.25:
        print(student_first_name, student_last_name, "made the Honor Roll.")
        