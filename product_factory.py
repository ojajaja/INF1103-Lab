"""Builds the right Product subclass from a saved record (SRP: creation from data).

OCP: a new product type is added with register_product_type(), without editing this
file's logic or Inventory.
"""
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product
from supplier import Supplier

_REGISTRY: dict[str, type[Product]] = {}


def register_product_type(product_class: type[Product]) -> None:
    _REGISTRY[product_class.TYPE] = product_class


register_product_type(PhysicalProduct)
register_product_type(DigitalProduct)


def create_product(record: dict, supplier: Supplier) -> Product:
    """Create a product from a dictionary using its 'type' identifier."""
    product_class = _REGISTRY.get(record["type"])
    if product_class is None:
        raise ValueError(f"Unknown product type: {record['type']}")
    return product_class.from_dict(record, supplier)
