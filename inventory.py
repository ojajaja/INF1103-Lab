from product import Product
from product_factory import create_product
from supplier import Supplier

# Used for records saved before suppliers existed.
UNKNOWN_SUPPLIER_RECORD = {"id": "UNKNOWN", "name": "Unknown Supplier", "contact_email": "n/a"}


class Inventory:
    """Manages a collection of Product objects (physical or digital) (SRP: the collection, not the menu or files).

    Aggregation: the Inventory holds references to Products but does not create or own them.
    Removing a Product here does not destroy it.
    """

    LINE = "-" * 48

    def __init__(self) -> None:
        self.__products: list[Product] = []

    @property
    def products(self) -> list[Product]:
        """A copy of the collection, so callers cannot change the Inventory's list directly."""
        return list(self.__products)

    def add_product(self, product: Product) -> bool:
        """Add an existing Product. Returns False if the ID already exists."""
        if self.find_product(product.product_id) is not None:
            return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        """Remove the matching reference. The Product itself is untouched. False if not found."""
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        """Return the Product with the given ID (case-insensitive), or None."""
        for product in self.__products:
            if product.product_id.lower() == product_id.lower():
                return product
        return None

    def find_supplier(self, supplier_id: str) -> Supplier | None:
        """Return a Supplier already used by a product here (so it can be reused), or None."""
        for product in self.__products:
            if product.supplier.supplier_id.lower() == supplier_id.lower():
                return product.supplier
        return None

    def display_all(self) -> None:
        print("Current Inventory")
        print(self.LINE)
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            print(product)
        print(self.LINE)

    def display_all_products(self) -> None:
        """Full details of every product, via the Product abstraction (polymorphism)."""
        for product in self.__products:
            product.display_information()
            print(product.get_fulfilment_info())
            print(self.LINE)

    def to_list(self) -> list[dict[str, object]]:
        """Return all products as a list of dictionaries (for saving)."""
        return [product.to_dict() for product in self.__products]

    def load_from_list(self, records: list[dict]) -> None:
        """Build Product objects from saved dictionaries.

        Records with the same supplier id share one Supplier object.
        """
        suppliers: dict[str, Supplier] = {}
        for r in records:
            s = r.get("supplier") or UNKNOWN_SUPPLIER_RECORD
            supplier = suppliers.get(s["id"])
            if supplier is None:
                supplier = Supplier.from_dict(s)
                suppliers[s["id"]] = supplier
            self.add_product(create_product(r, supplier))
