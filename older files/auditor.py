total_inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or 'quit' to stop): ").strip()

    if user_input.lower() == "quit":
        print("Exiting program...")
        break

    if not user_input.isdigit():
        print(f"Error: '{user_input}' is not a valid integer. Please try again.")
        failed_entries += 1
        continue

    quantity = int(user_input)

    if quantity < 0:
        print("Error: Negative stock quantities are not allowed.")
        failed_entries += 1
        continue

    total_inventory += quantity

    if total_inventory > 500:
        print(f"ALERT: Overstock detected! Total inventory is {total_inventory}, which exceeds 500 units.")
        break
    elif total_inventory == 500:
        print("Notice: Inventory has reached the maximum allowed (500 units).")
    else:
        print(f"Accepted. Current total inventory: {total_inventory}")

print("\n--- Inventory Audit Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")