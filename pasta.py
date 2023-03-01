from order import Order

class Pasta(Order):
    def __init__(self, order: str, price: int) -> None:
        super().__init__(order, price)