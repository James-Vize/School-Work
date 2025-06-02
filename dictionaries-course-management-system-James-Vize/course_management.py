"""
Course Management System:

This script provides a simple course management system implemented in Python.
It allows for the addition, removal, and checking of courses in a dictionary-based data structure.
"""

# Initialize an empty dictionary to store course information
course_info = {}

while True:
    print("\nCourse Management System")
    print("1. Display Course Names")
    print("2. Add New Course")
    print("3. Remove Course")
    print("4. Check Course Existence")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("Available Courses:")
        # Iterate through the course_info dictionary and print the course code and name for each course
        if course_info:
            for code, name in course_info.items():
                print(f"{code}: {name}")
        else:
            print("No courses available.")
    elif choice == '2':
        # Prompt the user for a course code and name, then add the course to the course_info dictionary
        # The course code should be converted to uppercase before being added to the dictionary
        course_code = input("Enter the course code: ").upper()
        if course_code in course_info:
            print(f"Course '{course_code}' already exists.")
        else:
            course_name = input("Enter the course name: ")
            course_info[course_code] = course_name
            print(f"Course '{course_code}' added successfully!")
    elif choice == '3':
        # Prompt the user for a course code to remove, then remove the course from the course_info dictionary
        # Python dictionary keys are case-sensitive, so the course code should be converted to uppercase before being removed
        # You must also make sure the course code exists in the dictionary before attempting to remove it.
        course_code = input("Enter the course code to remove: ").upper()
        if course_code in course_info:
            del course_info[course_code]
            print(f"Course '{course_code}' removed successfully!")
        else:
            print(f"Course '{course_code}' not found.")
    elif choice == '4':
        # Prompt the user for a course code to check, then check if the course exists in the course_info dictionary
        # Again, the course code should be converted to uppercase before being checked
        course_code = input("Enter the course code to check: ").upper()
        if course_code in course_info:
            print(f"Course '{course_code}' exists.")
        else:
            print(f"Course '{course_code}' does not exist.")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

