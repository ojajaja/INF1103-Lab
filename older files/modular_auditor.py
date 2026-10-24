def get_valid_input():
    while True:
        user_input = input("Enter stock quantity (or 'quit' to stop): ").strip()

        if user_input.lower() == "quit":
            return "quit"

        if not user_input.isdigit():
            print(f"Error: '{user_input}' is not a valid integer. Please try again.")
            return None

        quantity = int(user_input)
        return quantity


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("\n--- Delivery Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    total_inventory = 0
    failed_entries = 0
    deliveries_processed = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            print("Exiting program...")
            break

        if result is None:
            failed_entries += 1
            continue

        quantity = result
        total_inventory = process_delivery(total_inventory, quantity)
        tax = calculate_tax(quantity)
        deliveries_processed += 1

        if total_inventory > 500:
            print(f"ALERT: Overstock detected! Total inventory is {total_inventory}, which exceeds 500 units.")
            break
        elif total_inventory == 500:
            print("Notice: Inventory has reached the maximum allowed (500 units).")
        else:
            print(f"Accepted. Delivery: {quantity}, Tax: {tax:.2f}, "f"Running total: {total_inventory}")
        
    generate_report(deliveries_processed, failed_entries)


if __name__ == "__main__":
    main()