from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract base for all products (SRP: the state and behaviour common to every product)."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # ---------- Read-only access ----------
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    # ---------- Behaviour ----------
    def update_stock(self, quantity):
        """Set the stock to a new quantity. Returns True if accepted, False if rejected."""
        if not isinstance(quantity, int) or quantity < 0:
            return False
        self.__stock = quantity
        return True

    def display_information(self):
        """Print the details common to every product."""
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        """Return a message describing how this product is fulfilled."""
        pass

    def to_dict(self):
        """Return the common data as a dictionary (subclasses add their own fields)."""
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}

    def __str__(self):
        return (f"ID: {self.__product_id} | Name: {self.__name} | "
                f"Price: ${self.__price:.2f} | Stock: {self.__stock}")
    