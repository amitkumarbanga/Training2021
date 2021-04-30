class Dish:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def show_dish(self):
        print("^^^^^^^dish^^^^^^^")
        print("________________________")
        print("| {} | {} | {} |".format(self.name, self.price, self.rating))
        print("________________________")

class Menu:

    def __init__(self, title, num_of_dishes, dishes):
        self.title = title
        self.name_of_dishes = num_of_dishes
        self.dishes = dishes

    def show_menu(self):
        print("^^^^^^^MENU^^^^^^^")
        print("________________________")
        print("| {} | {} | {} |".format(self.title, self.name_of_dishes, self.dishes))
        print("________________________")

        print("DISHES: ")
        for dish in self.dishes:
            dish.show_dish()

class Restaurant:

    def __init__(self, name, phone, address, description, rating, menu):
        self.name = name
        self.phone = phone
        self.address = address
        self.description = description
        self.rating = rating
        self.menu = menu

    def show_restaurant(self):
        print("^^^^^^^RESTAURANT^^^^^^^")
        print("________________________")
        print("| {} | {} |".format(self.name, self.phone,))
        print("| {} | {} |".format(self.address, self.description))
        print(self.rating)
        print("________________________")
        self.menu.show_menu()

def main():

    dish1 = Dish(name="Samosa", price="45", rating="4.5")
    dish2 = Dish(name="Pizza", price="350", rating="4.3")
    dish3 = Dish(name="Brownie", price="200", rating="4.0")
    dish4 = Dish(name="Mack_puff", price="30", rating="4.2")
    dish5 = Dish(name="Garlic_bread", price="250", rating="4.6")

    dishes = [dish1, dish2, dish3, dish4, dish5]

    menu = Menu(title="Veg Indian Food", num_of_dishes=len(dishes), dishes=dishes)

    restaurant = Restaurant(name="Amar Sweets", phone="+91 8699988867", address="Jodhewal Basti", description="mithai, bakery, india etc.", rating=4.7, menu=menu)

    restaurant.show_restaurant()

if __name__ == '__main__':
    main()