from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored and shipped. Is-a Product; can be shipped."""

    TYPE = "physical"
    BASE_SHIPPING = 5.00
    RATE_PER_KG = 2.00

    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, weight: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight  # kilograms

    @property
    def weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self) -> str:
        return "Physical product: requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        """Flat base fee plus a rate per kilogram."""
        return self.BASE_SHIPPING + self.RATE_PER_KG * self.__weight

    def to_dict(self) -> dict[str, object]:
        data = super().to_dict()
        data["type"] = self.TYPE
        data["weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, r: dict, supplier: Supplier) -> "PhysicalProduct":
        return cls(r["id"], r["name"], float(r["price"]), int(r["stock"]),
                   supplier, float(r["weight"]))

    def __str__(self) -> str:
        return f"{super().__str__()} | Type: Physical | Weight: {self.__weight:.2f} kg"