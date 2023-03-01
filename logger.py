

class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0
    

    def log_transaction(self, order, store_number):
        self.transaction_count += 1
        self.daily_sales += order.price
        doc = open("log.txt", "a")
        doc.write(f"""\nCurrent transaction count: {self.transaction_count}
        Dish Ordered: {order.dish_name}
        Store Number: {store_number}
        Item Price: {order.price}
        Combined Daily Income: {self.daily_sales}\n\n""")
        doc.close()

log = Logger()

