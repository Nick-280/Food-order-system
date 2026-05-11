from dataclasses import dataclass, field

@dataclass
class Order:
    order_id: int = None
    address: str = ""
    discount_code: str = ""
    payment_method: str = ""
    special_note: str= ""
    notification_type: str= ""
    items: list = field(default_factory=list)
    total_price: float = 0

    def get_final_price(self) -> int:
        if self.discount_code == "FOOD20":
            return self.total_price * 80//100
        return self.total_price

    def add_item(self, name, price):
        item= {"name": name, "price": price}
        self.items.append(item)
        self.total_price += price

    def __str__(self) -> str:
        result = ""
        result += f"Order #{self.order_id}\n"
        result += f"Address: {self.address}\n"
        if self.discount_code:
            result += f"Discount Code: {self.discount_code}\n"
        result += f"Payment Method: {self.payment_method}\n"
        if self.special_note:
            result += f"Special Note: {self.special_note}\n"
        result += f"Notification: {self.notification_type}\n"
        result += f"Total Price: {self.get_final_price():,} IRR"
        return result

