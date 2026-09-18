def get_valid_input():
    """Prompt for a stock quantity. Returns a valid int, or 'quit'."""
    while True:
        user_input = input("Enter stock quantity (or 'quit' to stop): ").strip()

        if user_input.lower() == "quit":
            return "quit"

        if not user_input.isdigit():
            print(f"Error: '{user_input}' is not a valid integer. Please try again.")
            return None  # signals "invalid" back to caller, not a full retry loop

        quantity = int(user_input)
        return quantity


def process_delivery(current_total, new_value):
    """Add a delivery to the running total and return the new total."""
    return current_total + new_value


def calculate_tax(amount):
    """Return 10% tax on a single delivery amount."""
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    """Print the final summary."""
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

        print(f"Accepted. Delivery: {quantity}, Tax: {tax:.2f}, "
              f"Running total: {total_inventory}")

    generate_report(deliveries_processed, failed_entries)


if __name__ == "__main__":
    main()