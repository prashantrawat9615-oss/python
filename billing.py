"""Invoice creation and billing calculations."""
from validators import get_float, get_int, get_name


def billing_menu(bills):
    while True:
        print("\n--- BILLING SYSTEM ---\n1. Create bill\n2. Back to main menu")
        choice = input("Enter your choice (1-2): ").strip()
        if choice == "1":
            number = f"B-{len(bills) + 1:04d}"
            customer = get_name("Customer name: ")
            items = []
            while True:
                item_name = input("Item name (or press Enter to finish): ").strip()
                if not item_name:
                    if items: break
                    print("Please enter at least one item.")
                    continue
                items.append({"name": item_name, "price": get_float("Price: ", 0.01), "quantity": get_int("Quantity: ", 1)})
            subtotal = sum(i["price"] * i["quantity"] for i in items)
            discount = subtotal * 0.05
            taxable = subtotal - discount
            tax = taxable * 0.18
            total = taxable + tax
            print("\n==================== INVOICE ====================")
            print(f"Bill No: {number}     Customer: {customer}\n-------------------------------------------------")
            print(f"{'Item':<20} {'Price':>8} {'Qty':>5} {'Total':>10}")
            for i in items:
                print(f"{i['name']:<20} {i['price']:>8.2f} {i['quantity']:>5} {i['price'] * i['quantity']:>10.2f}")
            print("-------------------------------------------------")
            for label, value in [("Subtotal", subtotal), ("Discount (5%)", -discount), ("Taxable amount", taxable), ("Tax (18%)", tax)]:
                print(f"{label:<34} {value:>10.2f}")
            print(f"-------------------------------------------------\n{'GRAND TOTAL':<34} {total:>10.2f}\n=================================================\nThank you for your purchase!")
            bills.append({"number": number, "customer": customer, "subtotal": subtotal, "total": total})
        elif choice == "2": return
        else: print("Invalid choice. Enter 1 or 2.")
