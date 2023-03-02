from logger import log
from order_factory import Order_Factory
from verify import Verify


class Franchise:
    def __init__(self, location_number: int) -> None:
        self.location_number = location_number

    def place_order(self):
        print(f"\nWelcome to Lou Malnati's Pizza, Location #{self.location_number}\n")
        # user_input = Verify.verify_food_input(input("Would you like to order '1' for Pizza, '2' for Pasta, '3' or Salad?\n"))       
        # user_input = self.input_to_item(user_input)
        # order = Order_Factory.create_order(user_input)
        order = self.customer_order()
        log.log_transaction(order, self.location_number)



    #changes user input into chosen menu item
    def input_to_item(self, user_input):
        if user_input == '1':
            return "pizza"
        elif user_input == '2':
            return "pasta"
        elif user_input == '3':
            return "salad"
        
    def customer_order(self):
        user_input = ''
        order_list = []
        while user_input is not "4":
            user_input = Verify.verify_food_input(input("Would you like to order '1' for Pizza, '2' for Pasta, '3' for Salad?\nPress '4' to complete your order\n"))
            if user_input is not "4":
                user_input = self.input_to_item(user_input)
                order = Order_Factory.create_order(user_input)
                order_list.append(order)

        return order_list

            


        

#Welcome user, what items would you like to order?
#Loop to keep offering 3 options, a finished option
#that itemized order, maybe showing 2X Pizza, 1 Pasta, etc, that is what is put into log
#