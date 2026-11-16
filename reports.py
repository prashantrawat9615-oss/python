"""Cross-module summary report."""


def reports_menu(expenses, attendance_records, grade_reports, bills):
    print("\n--- SYSTEM REPORTS ---")
    print(f"Expenses recorded: {len(expenses)}")
    print(f"Total expenses: {sum(x['amount'] for x in expenses):.2f}")
    print(f"Attendance records: {len(attendance_records)}")
    if attendance_records:
        print(f"Average attendance: {sum(r['percentage'] for r in attendance_records) / len(attendance_records):.2f}%")
    print(f"Report cards created: {len(grade_reports)}")
    if grade_reports: print("Students:", ", ".join(r["name"] for r in grade_reports))
    print(f"Bills created: {len(bills)}")
    print(f"Total billed: {sum(b['total'] for b in bills):.2f}")
    input("Press Enter to return to the main menu...")
