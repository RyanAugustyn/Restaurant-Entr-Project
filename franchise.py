from logger import Logger
from order_factory import Order_Factory


class Franchise:
    def __init__(self, location_number: int) -> None:
        self.location_number = location_number

    def place_order(self):
        pass