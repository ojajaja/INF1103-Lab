from order_line import OrderLine
from product import Product


class Order:
    """A customer order. Composition: the Order creates and manages its own OrderLines.

    OrderLines are never passed in from outside and never handed to another Order.
    """

    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    @property
    def order_id(self) -> str:
        return self.__order_id

    @property
    def order_lines(self) -> tuple[OrderLine, ...]:
        """Read-only view: lines can only be added or removed through Order methods."""
        return tuple(self.__order_lines)

    def add_order_line(self, product: Product, quantity: int) -> None:
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: str) -> bool:
        """Remove the line for a product. The line goes with it; the Product is unaffected."""
        for line in self.__order_lines:
            if line.product.product_id == product_id:
                self.__order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.__order_lines)

    def display_order(self) -> None:
        print(f"Order {self.__order_id}")
        for line in self.__order_lines:
            print(f"  {line}")
        print(f"  Total: ${self.calculate_total():.2f}")
