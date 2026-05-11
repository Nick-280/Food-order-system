class Payment:
    def __init__(self, amount):
        self.amount= amount

    def pay(self):
        raise NotImplementedError("Payment method must implement pay()")
    
class OnlinePayment(Payment):
    def pay(self):
        print(f"Processing online payment of {self.amount} IRR")

class CashPayment(Payment):
    def pay(self):
        print(f"Cash payment of {self.amount} IRR will be collected on delivery")
        