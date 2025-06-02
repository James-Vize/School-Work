# Lab: Course Management with Dictionaries

## Description 

In this lab you will complete the provided `course_management.py` file by providing code where comments indicate "TODO".

Each course consists of a course code and name. The application shall allow the user to:

1. Display course names for any courses in the system.
2. Add a new course. If the course has already been added, duplicates should not be added.
3.  Remove a course. Don't forget to test the case where the course doesn't exist.
4. Check for existence of a course in the system.
5. Exist the program.

All course codes entered by the user should be converted to uppercase, even if entered in lowercase - e.g. if the user enters "infm109" you must add the key "INFM109" to the dictionary. Take this into account when checking if an entry exists in the dictionary.

## Output

**Output must match the provided output exactly.** This includes capitalization, punctuation, and spacing. Your output will be compared to the output in the text run character for character.

A full run covering all test cases is given below, however you should also test any additional common scenarios such as adding and printing multiple courses.

_Example Run:_

```
Course Management System
1. Display Course Names
2. Add New Course
3. Remove Course
4. Check Course Existence
5. Exit
Enter your choice (1-5): 2

Enter the course code: SDEV140
Enter the course name: Introduction to Software Development
Course 'SDEV140' added successfully!

Course Management System
1. Display Course Names
2. Add New Course
3. Remove Course
4. Check Course Existence
5. Exit
Enter your choice (1-5): 2

Enter the course code: SDEV140
Course 'SDEV140' already exists.

Course Management System
1. Display Course Names
2. Add New Course
3. Remove Course
4. Check Course Existence
5. Exit
Enter your choice (1-5): 4

Enter the course code to check: SDEV140
Course 'SDEV140' exists.

Course Management System
1. Display Course Names
2. Add New Course
3. Remove Course
4. Check Course Existence
5. Exit
Enter your choice (1-5): 1

Available Courses:
SDEV140: Introduction to Software Development

Course Management System
1. Display Course Names
2. Add New Course
3. Remove Course
4. Check Course Existence
5. Exit
Enter your choice (1-5): 3

Enter the course code to remove: SDEV140
Course 'SDEV140' removed successfully!

Course Management System
1. Display Course Names
2. Add New Course
3. Remove Course
4. Check Course Existence
5. Exit
Enter your choice (1-5): 3

Enter the course code to remove: SDEV140
Course 'SDEV140' not found.

Course Management System
1. Display Course Names
2. Add New Course
3. Remove Course
4. Check Course Existence
5. Exit

Course Management System
1. Display Course Names
2. Add New Course
3. Remove Course
4. Check Course Existence
5. Exit
Enter your choice (1-5): 4

Enter the course code to check: SDEV140
Course 'SDEV140' does not exist.

Course Management System
1. Display Course Names
2. Add New Course
3. Remove Course
4. Check Course Existence
5. Exit
Enter your choice (1-5): 5

Exiting the program. Goodbye!
```
