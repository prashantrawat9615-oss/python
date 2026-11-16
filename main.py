"""Entry point for the school and shop management system."""
from attendance import attendance_menu
from billing import billing_menu
from expenses import expense_menu
from grading import grading_menu
from reports import reports_menu


def main():
    expenses, attendance_records, grade_reports, bills = [], [], [], []
    try:
        while True:
            print("\n====================================\n     SCHOOL AND SHOP MANAGEMENT\n====================================")
            print("1. Expense Management\n2. Attendance Management\n3. Grading System\n4. Billing System\n5. View Reports\n6. Exit")
            choice = input("Enter your choice (1-6): ").strip()
            if choice == "1": expense_menu(expenses)
            elif choice == "2": attendance_menu(attendance_records)
            elif choice == "3": grading_menu(grade_reports)
            elif choice == "4": billing_menu(bills)
            elif choice == "5": reports_menu(expenses, attendance_records, grade_reports, bills)
            elif choice == "6":
                print("Thank you for using the system. Goodbye!")
                break
            else: print("Invalid choice. Enter a number between 1 and 6.")
    except KeyboardInterrupt:
        print("\nInput cancelled. Exiting the system.")
    finally:
        print("Session ended.")


if __name__ == "__main__":
    main()
