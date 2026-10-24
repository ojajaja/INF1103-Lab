from product import Product


class Inventory:
    """Manages a collection of Product objects (SRP: the collection, not the menu or files)."""

    LINE = "-" * 48

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Add a Product. Returns False if the ID already exists."""
        if self.search_product(product.product_id) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return the Product with the given ID (case-insensitive), or None."""
        for product in self.__products:
            if product.product_id.lower() == product_id.lower():
                return product
        return None

    def display_all(self):
        print("Current Inventory")
        print(self.LINE)
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            print(product)
        print(self.LINE)

    def to_list(self):
        """Return all products as a list of dictionaries (for saving)."""
        return [product.to_dict() for product in self.__products]

    def load_from_list(self, records):
        """Build Product objects from a list of dictionaries (from a loaded file)."""
        for r in records:
            self.add_product(Product(r["id"], r["name"], float(r["price"]), int(r["stock"])))
