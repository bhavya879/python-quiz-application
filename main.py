from admin import admin_menu 
from students import student_session 
from admin import admin_login,admin_menu
from students import student_session
from questions import return_questions
all_questions=return_questions()
def show_main_menu():
    print("\n" + "="*40)
    print(" PYTHON QUIZ APPLICATION")
    print("="*40)
    print("1. Admin Login")
    print("2. Student Login")
    print("3. Exit")
    choice = input("\nEnter Choice: ")
    return choice

while True:
    choice = show_main_menu()
    if choice == "1":
        username=input('Enter the Admin Username : ')
        password=input('Enter the Admin Password : ')
        
        if admin_login(username,password):
            admin_menu()
    elif choice == "2":
        student_session(all_questions)
    elif choice == "3":
        print("\nThank You For Using Python Quiz Application.")
        break 
    else:
        print("Invalid Choice!")