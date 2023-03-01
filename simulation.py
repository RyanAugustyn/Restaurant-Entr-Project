from franchise import Franchise

class Simulation:
    

    def run_simulation(self):
        store_one = Franchise(1)
        store_two = Franchise(2)
        store_three = Franchise(3)

        store_one.place_order()
        store_one.place_order()
        store_two.place_order()
        store_two.place_order()
        store_three.place_order()
        store_three.place_order()