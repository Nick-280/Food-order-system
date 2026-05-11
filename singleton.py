import threading

class RestaurantManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls) -> 'RestaurantManager':
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.orders = []
                    cls._instance.order_counter = 1000
        return cls._instance
    
    def add_order(self, order) -> int:
        self.order_counter += 1
        order.order_id = self.order_counter
        self.orders.append(order)
        return order.order_id
    
    def get_orders(self) -> list:
        return self.orders 
    
    @classmethod
    def get_instance(cls) -> 'RestaurantManager':
        return cls()
    
    