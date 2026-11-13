"""Lab 8 demonstration: association, aggregation, composition, LSP and polymorphism.

Run with:  python test_lab8.py
"""
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


def heading(text: str) -> None:
    print(f"\n=== {text} ===")


def show_product_details(product: Product) -> None:
    """Works for ANY Product: relies only on what Product promises (LSP)."""
    product.display_information()
    print(product.get_fulfilment_info())


# ---------- 2. Association ----------
heading("Association: Supplier and Product")
supplier = Supplier("S1", "Acme Supplies", "sales@acme.com")
laptop = PhysicalProduct("P1", "Laptop", 1200.0, 10, supplier, 2.5)
ebook = DigitalProduct("D1", "E-book", 15.0, 100, supplier, 5.0)

laptop.supplier.display_information()
ebook.supplier.display_information()

del supplier  # only removes the name 'supplier'; the object lives on through the products
print("After del supplier ->", laptop.supplier.name, "/", ebook.supplier.name)
assert laptop.supplier is ebook.supplier  # one shared Supplier object, not copies

# ---------- 3. Aggregation ----------
heading("Aggregation: Inventory and Product")
inv_a, inv_b = Inventory(), Inventory()
inv_a.add_product(laptop)
inv_a.add_product(ebook)
assert inv_a.remove_product("P1") is True
assert inv_a.find_product("P1") is None
print("Removed from Inventory A, still usable:", laptop)
laptop.update_stock(8)
inv_b.add_product(laptop)
assert inv_b.find_product("P1") is laptop  # the same object moved, not a copy
print("Now in Inventory B:", inv_b.find_product("P1"))

# ---------- 4. Composition ----------
heading("Composition: Order and OrderLine")
order1, order2 = Order("O1"), Order("O2")
order1.add_order_line(laptop, 2)
order1.add_order_line(ebook, 3)
order1.display_order()
assert order1.calculate_total() == 1200.0 * 2 + 15.0 * 3

order2.add_order_line(laptop, 1)  # same Product, different Order
line1, line2 = order1.order_lines[0], order2.order_lines[0]
assert line1 is not line2            # two OrderLine objects
assert line1.product is line2.product  # one Product object
print("OrderLine objects:", id(line1) != id(line2), "| shared Product object:", line1.product is line2.product)

order1.remove_order_line("D1")
print("After removing the E-book line from O1, E-book still exists:", ebook)
order1.display_order()

# ---------- 6 & 7. LSP and polymorphism ----------
heading("LSP and polymorphism")
inv = Inventory()
inv.add_product(laptop)
inv.add_product(ebook)
for p in inv.products:  # no isinstance() anywhere
    show_product_details(p)
    print("-" * 20)
for p in inv.products:
    assert p.update_stock(5) is True and p.stock == 5   # same meaning in both subclasses
    assert p.update_stock(-1) is False and p.stock == 5  # same rejection rule in both
print("update_stock behaves the same for both subclasses.")
print("\nAll Lab 8 checks passed.")
