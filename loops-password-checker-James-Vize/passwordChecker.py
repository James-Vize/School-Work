#James Vize, Password Checker. 


#Variables and Constants
CORRECT_PASSWORD = "correct"
MAX_ATTEMPTS = 3
password_correct = False
attempts = 0

#While loop so user can keep enterring passwords
while attempts < MAX_ATTEMPTS:
    password = input("Enter your password: ")

    if password == CORRECT_PASSWORD:
        print("Sucess!")
        password_correct = True
    #else loop that adds to the attempts if password is wrong. Also checks how many attempts there were.
    else:
        attempts += 1
        if attempts < MAX_ATTEMPTS:
            print("Incorrect password: ")
        else:
            print("Account locked.")

    #checks to see if the password that was entered was correct and then breaks out of the loop.
    if password_correct:
        break