from product import Product


class DigitalProduct(Product):
    """A product delivered by download. Is-a Product (not shippable)."""

    TYPE = "digital"

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size  # megabytes

    @property
    def download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")

    def get_fulfilment_info(self):
        return "Digital product: delivered digitally via download."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["download_size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, r):
        return cls(r["id"], r["name"], float(r["price"]), int(r["stock"]),
                   float(r["download_size"]))

    def __str__(self):
        return f"{super().__str__()} | Type: Digital | Download Size: {self.__download_size:.2f} MB"