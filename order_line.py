from product import Product


class OrderLine:
    """One product and quantity inside an Order.

    Composition part: created only by Order.add_order_line(). It refers to a Product
    (association) but does not own it.
    """

    def __init__(self, product: Product, quantity: int) -> None:
        self.__product: Product = product
        self.__quantity: int = quantity

    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.price * self.__quantity

    def __str__(self) -> str:
        return (f"{self.__product.name} x {self.__quantity} @ "
                f"${self.__product.price:.2f} = ${self.calculate_subtotal():.2f}")
