"""Attendance recording and display."""
from validators import get_int, get_name


def attendance_menu(records):
    while True:
        print("\n--- ATTENDANCE MANAGEMENT ---\n1. Record attendance\n2. View attendance records\n3. Back to main menu")
        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            name = get_name("Student name: ")
            total = get_int("Total class days: ", 1)
            present = get_int("Days present: ", 0)
            if present > total:
                print("Days present cannot be greater than total class days.")
                continue
            percentage = present / total * 100
            status = "Eligible" if percentage >= 75 else "Warning" if percentage >= 60 else "Shortage"
            records.append({"name": name, "total": total, "present": present,
                            "percentage": percentage, "status": status})
            print(f"Attendance: {percentage:.2f}% - {status}")
        elif choice == "2":
            if not records:
                print("No attendance records have been entered.")
            else:
                print("\nStudent          Present/Total    Attendance     Status\n" + "-" * 60)
                for r in records:
                    print(f"{r['name']:<17} {r['present']:>3}/{r['total']:<10} {r['percentage']:>7.2f}%     {r['status']}")
                print(f"Average attendance: {sum(r['percentage'] for r in records) / len(records):.2f}%")
        elif choice == "3":
            return
        else:
            print("Invalid choice. Enter a number between 1 and 3.")
