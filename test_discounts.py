import inspect
import unittest

from discount_strategy import (BulkDiscount, DiscountStrategy, NoDiscount,
                               PercentageDiscount, StudentDiscount)
from order import Order
from product_factory import ProductFactory
from supplier import Supplier


def make_order(discount=None) -> Order:
    supplier = Supplier("S1", "Acme", "a@acme.com")
    item = ProductFactory.create("physical", "P1", "Item", 50.0, 10, supplier)
    order = Order("O1", discount) if discount else Order("O1")
    order.add_order_line(item, 5)  # 5 x 50 = 250
    return order


class TestDiscounts(unittest.TestCase):
    def test_default_is_no_discount(self):
        self.assertEqual(make_order().calculate_total(), 250.0)

    def test_bulk_discount(self):
        self.assertEqual(make_order(BulkDiscount(200, 20)).calculate_total(), 230.0)

    def test_bulk_below_threshold_unchanged(self):
        self.assertEqual(BulkDiscount(300, 20).apply(250.0), 250.0)

    def test_set_discount_changes_strategy(self):
        order = make_order(BulkDiscount(200, 20))
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225.0)

    def test_new_strategy_needs_no_change_to_order(self):
        order = make_order()
        order.set_discount(StudentDiscount())
        self.assertAlmostEqual(order.calculate_total(), 237.5)
        self.assertIsInstance(StudentDiscount(), DiscountStrategy)

    def test_order_has_no_discount_if_elif_logic(self):
        source = inspect.getsource(Order.calculate_total)
        self.assertNotIn("if ", source)
        self.assertNotIn("elif", source)

    def test_one_strategy_can_be_shared_by_two_orders(self):
        shared = PercentageDiscount(10)
        self.assertEqual(make_order(shared).calculate_total(),
                         make_order(shared).calculate_total())

    def test_invalid_strategy_values_rejected(self):
        with self.assertRaises(ValueError):
            PercentageDiscount(150)
        with self.assertRaises(ValueError):
            BulkDiscount(-1, 20)

    def test_no_discount_returns_total(self):
        self.assertEqual(NoDiscount().apply(99.0), 99.0)


if __name__ == "__main__":
    unittest.main()
