from abc import ABC, abstractmethod

from supplier import Supplier


class Product(ABC):
    """Abstract base for all products (SRP: the state and behaviour common to every product).

    Association: a Product refers to the Supplier it was given. It does not create or own it.
    """

    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    # ---------- Read-only access ----------
    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def supplier(self) -> Supplier:
        return self.__supplier

    # ---------- Behaviour ----------
    def update_stock(self, quantity: int) -> bool:
        """Set the stock to a new quantity. Returns True if accepted, False if rejected."""
        if not isinstance(quantity, int) or quantity < 0:
            return False
        self.__stock = quantity
        return True

    def display_information(self) -> None:
        """Print the details common to every product."""
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")
        self.__supplier.display_information()

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return a message describing how this product is fulfilled."""
        pass

    def to_dict(self) -> dict[str, object]:
        """Return the common data as a dictionary (subclasses add their own fields)."""
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock,
                "supplier": self.__supplier.to_dict()}

    def __str__(self) -> str:
        return (f"ID: {self.__product_id} | Name: {self.__name} | "
                f"Price: ${self.__price:.2f} | Stock: {self.__stock} | "
                f"Supplier: {self.__supplier}")
