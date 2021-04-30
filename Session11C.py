class FoodItem:

    food_item_count = 0
    total_quantity = 0
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def increment(self):
        FoodItem.total_quantity += 1
        self.quantity += 1

    def decrement(self):
        FoodItem.total_quantity -= 1
        self.quantity += 1

    def show_food_item(self):
        print()
        print("___________________")
        print("FoodItem: {} | {}".format(self.name, self.price))
        print("quantity {}".format(self.quantity))
        print("___________________")

    def show(self):
        print("Total food item:", FoodItem.food_item_count)
        print("Total quantity:", FoodItem.total_quantity)

def main():
    item1 = FoodItem("Burger", 200, 1)
    item2 = FoodItem("Sandwich", 100, 1)
    item3 = item1


    item1.show_food_item()
    item2.show_food_item()
    item3.show_food_item()

    item1.increment()
    item2.increment()
    item3.increment()

    item1.increment()
    item2.increment()

    item3.decrement()
    item1.decrement()

    item1.show_food_item()
    item2.show_food_item()
    item3.show_food_item()

    item1.show()
    item2.show()
    item3.show()

if __name__ == '__main__':
    main()