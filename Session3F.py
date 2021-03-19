menu = {
    "Football": 2400,
    "Bat": 1200,
    "Golf_kit": 10000,
    "Baseball": 2200,
    "Spikes": 1000,
    "Socks": 300,
    "Wickets": 600,
    "Gloves": 1200
}

print("Please start shopping from given items")
print(menu)

cart = []
choice = "yes"


# CONTROLLER

while choice == "yes":
    item = input("Enter your choice:")
    cart.append(menu[item])

    choice = input("Would you like to buy more? yes/no:")
print("your cart[{}]:".format(len(cart)))
print(cart)

total_amount = sum(cart)
print("total:", total_amount)

Promo_code = input("Enter Your PROMO_CODE:")
if Promo_code == "CRAVINGS":
    print("PROMO_CODE APPLIED")
print()

total_amount = total_amount - (0.5*total_amount)
print("total amount after PROMO_CODE APPLIED:", total_amount)

total_amount = total_amount + (0.18*total_amount)
print("After Taxes Applied:", total_amount)
