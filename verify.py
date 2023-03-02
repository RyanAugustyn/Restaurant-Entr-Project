class Verify:
    @staticmethod
    def verify_food_input(user_input):
        while user_input not in ["1", "2", "3", "4"]:
            print("Incorrect entry")
            user_input = input("Would you like to order '1' for Pizza, '2' for Pasta, '3' or Salad?\nPress 4 to complete your order\n")
        return user_input