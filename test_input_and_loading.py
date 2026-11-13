import contextlib
import io
import os
import tempfile
import unittest
from unittest import mock

from input_helpers import get_positive_float
from inventory import Inventory
from product_loader import load_products
from supplier import Supplier

CSV = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


def run(func, *args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        result = func(*args)
    return result, out.getvalue()


class TestPositiveFloat(unittest.TestCase):
    def test_asks_again_until_valid(self):
        with mock.patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
            value, output = run(get_positive_float, "Price: ")
        self.assertEqual(value, 12.5)
        self.assertIn("Please enter a valid number", output)
        self.assertIn("greater than zero", output)


class TestLoadProducts(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S1", "Acme", "a@acme.com")
        self.inventory = Inventory()

    def test_bad_rows_skipped_valid_rows_loaded(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "products.csv")
            with open(path, "w") as f:
                f.write(CSV)
            _, output = run(load_products, path, self.inventory, self.supplier)
        self.assertEqual(len(self.inventory.products), 3)
        self.assertIn("Unknown product type: service", output)
        self.assertIn("3 products loaded.", output)
        self.assertTrue(output.rstrip().endswith("Load attempt finished."))

    def test_missing_file_handled(self):
        _, output = run(load_products, "no_such_file.csv", self.inventory, self.supplier)
        self.assertIn("Products file not found", output)
        self.assertIn("Load attempt finished.", output)
        self.assertNotIn("products loaded", output)
        self.assertEqual(self.inventory.products, [])


if __name__ == "__main__":
    unittest.main()
