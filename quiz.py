def show_instructions():
    print("\n" + "="*40)
    print("   QUIZ IN STRUCTIONS   ")
    print("="*40)
    print("1. The quiz contains 15 questions.")
    print("2. Each question carries 1 mark.")
    print("3. There is no negative marking.")
    print("4. Enter only A, B, C or D.")
    print("5. Once answered, a question cannot be revisited.")
    confirmation = input(
        "\nHave you read the instructions? (Y/N): ").upper()
    return confirmation == 'Y'

def calculate_percentage(score, total_qstns):
    return round((score / total_qstns) * 100,2)

def ask_question(qstn_dict):
    print("\n")
    print(qstn_dict["question"])
    for option in qstn_dict["options"]:
        print(option)
    answer = input("\nEnter Answer (A/B/C/D): ").upper()
    while answer not in ['A', 'B', 'C', 'D']:
        answer = input("Please enter A/B/C/D only: ").upper()
    return answer
def assign_grade(percentage):
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Very Good"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 40:
        return "Average"
    return "Needs Improvement"

def show_result(name,score,total_qstns):
    percentage = calculate_percentage(score,total_qstns)
    grade = assign_grade(percentage)
    print("\n" + "="*40)
    print("            RESULT")
    print("="*40)
    print(f"Student: {name}")
    print(f"Score: {score}/{total_qstns}")
    print(f"Percentag1e: {percentage}%")
    print(f"Grade: {grade}")
    
import random

def start_quiz(questions):
    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)
    ttl_qstns = 15
    score = 0
    for count in range(ttl_qstns):
        crnt_qstn = \
            quiz_questions[count]
        print(f"\nQuestion " f"{count+1} of " f"{ttl_qstns}")
        user_answer = ask_question(crnt_qstn)
        if user_answer==crnt_qstn["answer"]:
            print("Correct!")
            score += 1
        else:
            print(
                f"Incorrect!"
                f" Correct Answer: "
                f"{crnt_qstn['answer']}")
    return score