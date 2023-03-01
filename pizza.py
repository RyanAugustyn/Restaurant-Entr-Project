from order import Order

class Pizza(Order):
    def __init__(self, order: str, price: int) -> None:
        super().__init__(order, price)