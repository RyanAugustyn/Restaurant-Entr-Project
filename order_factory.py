from pizza import Pizza
from pasta import Pasta
from salad import Salad


class Order_Factory:

    @staticmethod
    def create_order(order: str):
        if order == "pizza":
            return Pizza()
        elif order == "pasta":
            return Pasta()
        elif order == "salad":
            return Salad()
