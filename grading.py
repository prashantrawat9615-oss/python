"""Student grade reports."""
from validators import get_float, get_name

SUBJECTS = ["Maths", "Science", "English", "History", "Computer"]


def get_grade(percentage):
    if percentage >= 90: return "A+"
    if percentage >= 80: return "A"
    if percentage >= 70: return "B"
    if percentage >= 60: return "C"
    if percentage >= 50: return "D"
    if percentage >= 35: return "E"
    return "F"


def grading_menu(reports):
    while True:
        print("\n--- GRADING SYSTEM ---\n1. Create report card\n2. Back to main menu")
        choice = input("Enter your choice (1-2): ").strip()
        if choice == "1":
            name = get_name("Student name: ")
            marks = {}
            for subject in SUBJECTS:
                marks[subject] = get_float(f"{subject} marks (0-100): ", 0)
                while marks[subject] > 100:
                    print("Marks cannot be more than 100.")
                    marks[subject] = get_float(f"{subject} marks (0-100): ", 0)
            total = sum(marks.values())
            average = total / len(SUBJECTS)
            percentage = total / (len(SUBJECTS) * 100) * 100
            grade = get_grade(percentage)
            result = "PASS" if percentage >= 35 else "FAIL"
            print("\n========== REPORT CARD ==========\nStudent:", name, "\nSubject                  Marks")
            for subject, mark in marks.items():
                print(f"{subject:<24} {mark:g}")
            print("---------------------------------")
            print(f"Total       : {total:g} / {len(SUBJECTS) * 100}\nAverage     : {average:.2f}\nPercentage  : {percentage:.2f}%\nGrade       : {grade}\nResult      : {result}\n=================================")
            reports.append({"name": name, "total": total, "percentage": percentage, "grade": grade, "result": result})
        elif choice == "2": return
        else: print("Invalid choice. Enter 1 or 2.")
