import json
import os

from product import Product
from inventory import Inventory

INVENTORY_FILE = "inventory.json"
LINE = "-" * 48


# ---------- File handling ----------
def load_inventory(inventory):
    """Load products from inventory.json into the Inventory object."""
    if os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} found.")
        try:
            with open(INVENTORY_FILE, "r") as f:
                records = json.load(f)
            inventory.load_from_list(records)
            print("Inventory loaded successfully.")
        except (json.JSONDecodeError, OSError, KeyError, ValueError, TypeError):
            print("Warning: could not read the file. Starting with an empty inventory.")
            inventory.__init__()  # reset to empty in case of a partial load
    else:
        print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")


def save_inventory(inventory):
    """Save the Inventory's products to inventory.json."""
    try:
        with open(INVENTORY_FILE, "w") as f:
            json.dump(inventory.to_list(), f, indent=4)
        print(f"Inventory saved successfully to {INVENTORY_FILE}.")
    except OSError as e:
        print(f"Error: could not save inventory ({e}).")


# ---------- Input helpers ----------
def get_valid_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print(f"Error: '{value}' is not a valid non-negative integer. Please try again.")


def get_valid_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
            if number >= 0:
                return number
        except ValueError:
            pass
        print(f"Error: '{value}' is not a valid price. Please try again.")


# ---------- Menu actions ----------
def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip()
    if not product_id:
        print("Error: Product ID cannot be empty.")
        return
    if inventory.search_product(product_id):
        print("Error: A product with that ID already exists.")
        return
    name = input("Product Name: ").strip()
    if not name:
        print("Error: Product name cannot be empty.")
        return
    price = get_valid_float("Price: ")
    stock = get_valid_int("Stock Quantity: ")

    inventory.add_product(Product(product_id, name, price, stock))
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print(f"Name: {product.name}")
    print(f"Current Stock: {product.stock}")
    product.update_stock(get_valid_int("New Stock Quantity: "))
    print("Stock updated successfully!")


def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print(LINE)
    product.display_information()
    print(LINE)


def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = Inventory()
    load_inventory(inventory)
    show_menu()

    while True:
        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
