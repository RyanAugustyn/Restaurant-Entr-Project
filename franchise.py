from logger import log
from order_factory import Order_Factory


class Franchise:
    def __init__(self, location_number: int) -> None:
        self.location_number = location_number

    def place_order(self):
        print(f"\nWelcome to Lou Malnati's Pizza, Location #{self.location_number}\n")
        user_input = input("Would you like to order '1' for Pizza, '2' for Pasta, '3' or Salad?\n")
        #error handling
        while user_input not in ["1", "2", "3"]:
            print("Incorrect entry")
            user_input = input("Would you like to order '1' for Pizza, '2' for Pasta, '3' or Salad?\n")
        if user_input == '1':
            user_input = "pizza"
        elif user_input == '2':
            user_input = "pasta"
        elif user_input == '3':
            user_input = "salad"
        
        order = Order_Factory.create_order(user_input)
        log.log_transaction(order, self.location_number)


