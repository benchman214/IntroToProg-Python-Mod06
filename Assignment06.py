# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   NDeAsis, 3/3/2025, Revised Script
#   NDeAsis, 3/4/2025, Revised Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Constants
"""
FILE_NAME = "Enrollments.json"

class FileProcessor:
    
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads student data from a JSON file and loads it into a list."""
        try:
            with open(file_name, 'r') as file:
                student_data.extend(json.load(file))
        except (FileNotFoundError, json.JSONDecodeError) as e:
            IO.output_error_messages("File not found or empty. Starting with an empty list.", e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes student data to a JSON file."""
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file, indent=4)
            print("Data saved successfully.")
            IO.output_student_courses(student_data)
        except IOError as e:
            IO.output_error_messages("Error saving data.", e)

class IO:
    """Handles input and output operations."""
    
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Outputs error messages to the user."""
        print(f"Error: {message}")
        if error:
            print(f"Details: {error}")
    
    @staticmethod
    def output_menu(menu: str):
        """Displays the main menu."""
        print(menu)
    
    @staticmethod
    def input_menu_choice():
        """Gets the user menu choice."""
        return input("Enter your choice: ").strip()
    
    @staticmethod
    def output_student_courses(student_data: list):
        """Displays registered students and their courses."""
        if student_data:
            for student in student_data:
                print(f"{student['first_name']}, {student['last_name']}, {student['course']}")
        else:
            print("No enrollments found.")
    
    @staticmethod
    def input_student_data(student_data: list):
        """Prompts user to input student details and adds them to the list."""
        try:
            first_name = input("Enter student's first name: ").strip()
            if not first_name:
                raise ValueError("First name cannot be empty.")
            last_name = input("Enter student's last name: ").strip()
            if not last_name:
                raise ValueError("Last name cannot be empty.")
            course = input("Enter course name: ").strip()
            student_data.append({"first_name": first_name, "last_name": last_name, "course": course})
        except ValueError as e:
            IO.output_error_messages("Input error.", e)

# Main Execution
students = []
FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(MENU)
    choice = IO.input_menu_choice()
    
    if choice == "1":
        IO.input_student_data(students)
    elif choice == "2":
        IO.output_student_courses(students)
    elif choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please select a valid option.")
"""
