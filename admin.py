def view_results():
    try:
        with open("quizresults.csv", "r") as file:
            print("\n")
            print("="*60)
            print("RESULTS")
            print("="*60)
            print(
                f"{'Roll No':<12}"
                f"{'Name':<20}"
                f"{'Score':<10}"
                f"{'Percentage':<10}"
                f"{'Grade':<15}")
            print("-"*60)
            for line in file:
                roll_no,name,score,total,percentage,grade =\
                    line.strip().split(",")
                print(
                    f"{roll_no:<12}"
                    f"{name:<20}"
                      f"{score}/{total:<10}"
                    f"{percentage:<10}"
                    f"{grade:<15}"
                )
    except FileNotFoundError:
        print("No results found.")
            
def view_leaderboard():
    try:
        students = []
        with open("quizresults.csv","r") as file:
            for line in file:
                roll_no,name,score,total,percentage,grade = \
                    line.strip().split(",")
                students.append((name,int(score)))
        students.sort(key=lambda x:x[1],reverse=True)
        print("\n")
        print("="*40)
        print("LEADERBOARD")
        print("="*40)
        rank = 1
        for student in students:
            print(
                f"{rank}. "
                f"{student[0]} "
                f"({student[1]} Marks)"
                f"{percentage}% "
                f"{grade}")
            rank += 1
    except FileNotFoundError:
        print("No results available.")


def admin_login(username,password):
    admin_credentials = {"QUIZMASTER": "12345"}
    if admin_credentials.get(username) == password:
        print('Log in Successfull ! ')
        return True
    else:
        print("You have entered the wrong credentials!")
        return False
    
def admin_menu():
    while True:
        print("\n")
        print("="*30)
        print("ADMIN MENU")
        print("="*30)
        print("1. View Results")
        print("2. Leaderboard")
        print("3. Print Results to excel")
        print("4. Logout")
        choice = input("\nEnter Choice: ")
        if choice == "1":
            view_results()
        elif choice == "2":
            view_leaderboard()
        elif choice == "3":
             print_results()   
        elif choice == "4":
            print("Logging Out...")
            break
        else:
            print("Invalid Choice")
            
import pandas as pd
import os
def print_results():
    path=input('Give the folder path to which the results needs to be saved : ').strip().strip('"')
    try:
        results=pd.read_csv("quizresults.csv",names=["Roll No", "Name", "Score", "Total","Percentage","Grade"])
        output_path = os.path.join(path, "QuizResults.xlsx")
        results.to_excel(output_path,index=False)
        print('Results have been successfully saved !')
    except FileNotFoundError:
        print("Sorry, results.csv is not available.")
    except Exception as e:
        print(f"An error occurred: {e}")
        

