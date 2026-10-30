from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored and shipped. Is-a Product; can be shipped."""

    TYPE = "physical"
    BASE_SHIPPING = 5.00
    RATE_PER_KG = 2.00

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight  # kilograms

    @property
    def weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        return "Physical product: requires physical shipping."

    def calculate_shipping_cost(self):
        """Flat base fee plus a rate per kilogram."""
        return self.BASE_SHIPPING + self.RATE_PER_KG * self.__weight

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, r):
        return cls(r["id"], r["name"], float(r["price"]), int(r["stock"]), float(r["weight"]))

    def __str__(self):
        return f"{super().__str__()} | Type: Physical | Weight: {self.__weight:.2f} kg"