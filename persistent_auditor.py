INVENTORY_FILE = "inventory.txt"


def load_inventory():

    total_inventory = 0
    history = []

    try:
        with open(INVENTORY_FILE, "r") as f:
            lines = f.read().splitlines()

        for line in lines:
            if line.startswith("TOTAL:"):
                value = line[len("TOTAL:"):].strip()
                total_inventory = int(value) if value else 0
            elif line.startswith("HISTORY:"):
                value = line[len("HISTORY:"):].strip()
                if value:
                    history = [int(x) for x in value.split(",")]

    except FileNotFoundError: #if no file
        total_inventory = 0
        history = []

    return total_inventory, history


def save_inventory(total_inventory, history):
    with open(INVENTORY_FILE, "w") as f:
        f.write(f"TOTAL:{total_inventory}\n")
        f.write("HISTORY:" + ",".join(str(x) for x in history) + "\n")


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
    total_inventory, transaction_history = load_inventory()
    if total_inventory or transaction_history:
        print(f"Loaded saved inventory: {total_inventory} units, "
              f"{len(transaction_history)} past transaction(s).")
    else:
        print("No saved inventory found. Starting fresh.")

    failed_entries = 0
    deliveries_processed = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            print("Exiting program...")
            save_inventory(total_inventory, transaction_history)
            print(f"Saved to {INVENTORY_FILE}.")
            break

        if result is None:
            failed_entries += 1
            continue

        quantity = result
        total_inventory = process_delivery(total_inventory, quantity)
        transaction_history.append(quantity)
        tax = calculate_tax(quantity)
        deliveries_processed += 1

        if total_inventory > 500:
            print(f"ALERT: Overstock detected! Total inventory is {total_inventory}, which exceeds 500 units.")
            save_inventory(total_inventory, transaction_history)
            print(f"Saved to {INVENTORY_FILE}.")
            break
        elif total_inventory == 500:
            print("Notice: Inventory has reached the maximum allowed (500 units).")
        else:
            print(f"Accepted. Delivery: {quantity}, Tax: {tax:.2f}, "f"Running total: {total_inventory}")

    generate_report(deliveries_processed, failed_entries)


if __name__ == "__main__":
    main()