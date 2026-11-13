from product import Product
from supplier import Supplier


class DigitalProduct(Product):
    """A product delivered by download. Is-a Product (not shippable)."""

    TYPE = "digital"

    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, download_size: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size  # megabytes

    @property
    def download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self) -> str:
        return "Digital product: delivered digitally via download."

    def to_dict(self) -> dict[str, object]:
        data = super().to_dict()
        data["type"] = self.TYPE
        data["download_size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, r: dict, supplier: Supplier) -> "DigitalProduct":
        return cls(r["id"], r["name"], float(r["price"]), int(r["stock"]),
                   supplier, float(r["download_size"]))

    def __str__(self) -> str:
        return f"{super().__str__()} | Type: Digital | Download Size: {self.__download_size:.2f} MB"