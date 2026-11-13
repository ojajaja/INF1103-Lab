import unittest

from digital_product import DigitalProduct
from order_line import OrderLine
from physical_product import PhysicalProduct
from product import Product
from product_factory import ProductFactory
from supplier import Supplier

SUPPLIER = Supplier("S1", "Acme", "a@acme.com")


class TestFactory(unittest.TestCase):
    def test_creates_physical(self):
        p = ProductFactory.create("physical", "P1", "Lamp", 25.0, 10, SUPPLIER, weight=2.0)
        self.assertIsInstance(p, PhysicalProduct)
        self.assertIsInstance(p, Product)

    def test_creates_digital(self):
        p = ProductFactory.create("digital", "D1", "App", 49.9, 100, SUPPLIER, download_size=5.0)
        self.assertIsInstance(p, DigitalProduct)

    def test_unknown_type_raises_clear_error(self):
        with self.assertRaises(ValueError) as ctx:
            ProductFactory.create("service", "S1", "Install", 30.0, 5, SUPPLIER)
        self.assertIn("Unknown product type: service", str(ctx.exception))


class TestValidation(unittest.TestCase):
    def test_price_must_be_positive(self):
        for bad in (0, -5.0):
            with self.assertRaises(ValueError):
                ProductFactory.create("physical", "P1", "Lamp", bad, 10, SUPPLIER)

    def test_stock_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D1", "App", 10.0, -1, SUPPLIER)

    def test_zero_stock_allowed(self):
        self.assertEqual(ProductFactory.create("digital", "D1", "App", 10.0, 0, SUPPLIER).stock, 0)

    def test_order_line_quantity_must_be_positive(self):
        product = ProductFactory.create("physical", "P1", "Lamp", 25.0, 10, SUPPLIER)
        for bad in (0, -2):
            with self.assertRaises(ValueError):
                OrderLine(product, bad)


if __name__ == "__main__":
    unittest.main()
