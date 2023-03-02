class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0
    

    def log_transaction(self, order, store_number):
        self.transaction_count += 1
        for item in order:
            self.daily_sales += item.price
            self.append_to_log(store_number, self.transaction_count, item, self.daily_sales)
        


    def append_to_log(self, store_number, transaction_count, order, daily_sales):
        doc = open("log.txt", "a")
        doc.write(f"""\nPurchase at Lou Malnati's store # {store_number}
        Current transaction count: {transaction_count}
        Dish Ordered: {order.dish_name}
        Item Price: {order.price}
        Combined Daily Income: {daily_sales}\n\n""")
        doc.close()

log = Logger()

