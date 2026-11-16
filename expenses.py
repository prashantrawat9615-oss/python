"""Expense recording and summaries."""
from validators import get_float


def expense_menu(expenses):
    while True:
        print("\n--- EXPENSE MANAGEMENT ---\n1. Add expense\n2. View all expenses\n3. Expense summary\n4. Back to main menu")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            description = input("Description: ").strip()
            category = input("Category (Food/Travel/Utilities/Stationery/Other): ").strip().title()
            amount = get_float("Amount: ", 0.01)
            expenses.append({"description": description, "category": category, "amount": amount})
            print("Expense added successfully!")
        elif choice == "2":
            if not expenses:
                print("No expenses have been recorded.")
            else:
                print(f"\n{'Description':<28} {'Category':<20} {'Amount':>8}\n{'-' * 58}")
                for item in expenses:
                    print(f"{item['description']:<28} {item['category']:<20} {item['amount']:>8.2f}")
        elif choice == "3":
            if not expenses:
                print("No expenses to summarize.")
                continue
            totals = {}
            for item in expenses:
                category = item["category"]
                totals[category] = totals.get(category, 0) + item["amount"]
            print("\nCATEGORY                 TOTAL")
            for category, total in totals.items():
                print(f"{category:<24} {total:>8.2f}")
            print(f"{'-' * 35}\n{'GRAND TOTAL':<24} {sum(x['amount'] for x in expenses):>8.2f}")
            high, low = max(expenses, key=lambda x: x["amount"]), min(expenses, key=lambda x: x["amount"])
            print(f"Highest expense: {high['category']} - {high['amount']:.2f} ({high['description']})")
            print(f"Lowest expense:  {low['category']} - {low['amount']:.2f} ({low['description']})")
        elif choice == "4":
            return
        else:
            print("Invalid choice. Enter a number between 1 and 4.")
