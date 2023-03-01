from logger import log
from order_factory import Order_Factory


class Franchise:
    def __init__(self, location_number: int) -> None:
        self.location_number = location_number

    def place_order(self):
        user_input = input("Would you like to order Pizza, Pasta, or Salad?")
        user_input.lower()
        #error handling
        while user_input not in ["pizza", "pasta", "salad"]:
            print("Incorrect entry")
            user_input = input("Would you like to order Pizza, Pasta, or Salad?")
            user_input.lower()
        order = Order_Factory.create_order(user_input)
        log.log_transaction(order, self.location_number)


