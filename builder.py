from models.order import Order

    
class OrderBuilder:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> 'OrderBuilder':
        self.order = Order()
        return self
    
    def set_address(self, address) -> 'OrderBuilder':
        if not address or len(address) < 5:
            raise ValueError("The address should have at least 5 characters")
        self.order.address = address
        return self
    
    def set_discount(self, code) -> 'OrderBuilder':
        if code in ["FOOD20", "SAVE10"]:
            self.order.discount_code = code
        return self
    
    def set_payment(self, method) -> 'OrderBuilder':
        if method not in ["Online Card", "Cash"]:
            raise ValueError("paying type must be wether in Cash or with Online Card")
        self.order.payment_method = method
        return self
    
    def set_note(self, note) -> 'OrderBuilder':
        self.order.special_note = note
        return self
    
    def set_notification(self, notif) -> 'OrderBuilder':
        if notif not in ["SMS", "Email"]:
            raise ValueError("The notification type must be SMS or Email")
        self.order.notification_type = notif
        return self
    
    def add_item(self, name, price) -> 'OrderBuilder':
        if price <= 0:
            raise ValueError("Invalid price")
        self.order.items.append({"name": name, "price": price})
        self.order.total_price += price
        return self
    
    def build(self) -> Order:
        if not self.order.address:
            raise ValueError("Address is required")
        if not self.order.payment_method:
            raise ValueError("Payment method is required")
        return self.order
        
class OrderDirector:
    def __init__(self, builder) -> None:
        self.builder = builder

    def make_standard_order(self, address, payment)-> Order:
        return (self.builder.reset().set_address(address).set_payment(payment).set_notification("SMS").build())
    
