from quiz import show_instructions,start_quiz,show_result,assign_grade

def calculate_percentage(score, total_qstns):
    return round((score / total_qstns) * 100,2)

def student_login():
    name = input("Please Enter Your Name: ")
    roll_no = input("Enter YourRoll Number: ")
    details ={"name": name,"roll_no": roll_no}
    print(f"\nWelcome {name}!")
    return details

def student_menu():
    print("\n" + "="*30)
    print("      STUDENT MENU")
    print("="*30)
    print("1. Start Quiz")
    print("2. View Instructions")
    print("3. Logout")
    return input("Enter Choice: ")

def student_session(questions):
    student = student_login()
    proceed = show_instructions()
    if not proceed:
        print("Quiz  Cancelled.")
        return
    score = start_quiz(questions)
    save_result(student["name"],student["roll_no"],score,15)
    show_result(student["name"],score,15)
    
def save_result(name,roll_no,score,total_questions):
    percentage = calculate_percentage(score,total_questions)
    grade = assign_grade(percentage)
    with open("quizresults.csv", "a") as file:
        file.write(f"{roll_no},{name},{score},{total_questions},{percentage},{grade}\n")