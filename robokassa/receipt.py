from dataclasses import dataclass, field, is_dataclass, asdict
from decimal import Decimal
import json
from typing import Any, List, Self
from urllib.parse import quote_plus

from robokassa.enums import Taxes


class ReceiptToJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)


@dataclass
class ReceiptItem:
    name: str
    quantity: int
    sum: Decimal
    tax: Taxes


@dataclass
class Receipt:
    items: List[ReceiptItem] = field(default_factory=list)

    def __str__(self) -> str:
        return json.dumps(self.items, cls=ReceiptToJSONEncoder)


class ReceiptBuilder:
    def __init__(self) -> None:
        self.__receipt = Receipt()

    def item(self, name: str, quantity: int, sum: Decimal, tax: Taxes) -> Self:
        self.__receipt.items.append(
            ReceiptItem(
                name=name,
                quantity=quantity,
                sum=sum,
                tax=tax,
            )
        )

        return self

    def to_url(self) -> str:
        return quote_plus(quote_plus(str(self)))

    def __str__(self) -> str:
        return str(self.__receipt)


if __name__ == "__main__":
    builder = ReceiptBuilder()
    builder.item(name="name", quantity=0, sum=0, tax=Taxes.NONE)
    print(builder)
    print(builder.to_url())
