def get_valid_input():
        entry = input("Enter stock quantity (enter quit to exit): ")

        if entry.lower() == "quit":
            return "quit"

        if not entry.isdigit():
            print("Invalid input. Please enter a valid number.")
            return None

        quantity = int(entry)

        if quantity < 0:
            print("Invalid input. Quantity cannot be negative.")
            return None

        return quantity

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax





