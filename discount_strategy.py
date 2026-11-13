from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    """Strategy interface: every discount turns an order total into a discounted total."""

    @abstractmethod
    def apply(self, total: float) -> float:
        """Return the discounted total."""
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    """Takes a percentage off the total, e.g. PercentageDiscount(10) takes 10% off."""

    def __init__(self, percentage: float) -> None:
        if not 0 <= percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.__percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.__percentage / 100)


class BulkDiscount(DiscountStrategy):
    """Takes a fixed amount off any total at or above a threshold, e.g. BulkDiscount(200, 20)."""

    def __init__(self, threshold: float, amount: float) -> None:
        if threshold < 0 or amount < 0:
            raise ValueError("Bulk discount threshold and amount cannot be negative.")
        self.__threshold: float = threshold
        self.__amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self.__threshold:
            return max(0.0, total - self.__amount)
        return total


class StudentDiscount(DiscountStrategy):
    """Fourth strategy: a flat 5% student discount. Added without touching Order."""

    RATE = 0.05

    def apply(self, total: float) -> float:
        return total * (1 - self.RATE)
