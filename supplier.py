class Supplier:
    """Who supplied a product. Associated with Product; owns nothing and is owned by nothing."""

    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    @property
    def supplier_id(self) -> str:
        return self.__supplier_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id}")
        print(f"Supplier Name: {self.__name}")
        print(f"Supplier Email: {self.__contact_email}")

    def to_dict(self) -> dict[str, str]:
        return {"id": self.__supplier_id, "name": self.__name,
                "contact_email": self.__contact_email}

    @classmethod
    def from_dict(cls, r: dict[str, str]) -> "Supplier":
        return cls(r["id"], r["name"], r["contact_email"])

    def __str__(self) -> str:
        return f"{self.__name} ({self.__supplier_id})"
