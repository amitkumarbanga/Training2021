amount = int(input("Enter Your Amount"))
"""if amount >= 500:
    print("You Are Eligible To Apply Promo_Code")
    print("Apply ZOMATO To Get 40% discount:")
    promo_code = input("Enter Your Promo_code")
    if promo_code == "ZOMATO":
        discount = 0.40*amount
        if discount >= 200:
            discount = 200
            print("Discount For You:")
            amount -= discount

        print("ZOMATO Promo_code Applied")
    else:
        ("Your Promo_code Is Invallied")

else:
    ("You Are Not Eligile To Enter Promo Code")
print("Please Pay \u20b9", amount")"""

if amount >= 100:
    promo_code = input("Enter Your Promo_code")

    if promo_code == "ZOMATO":
            discount = 0.40 * amount
            if discount >= 100:
               discount = 100
            print("ZOMATO Promo_Code", discount)
            amount -= discount

    if promo_code == "JUMBO":
        discount = 0.50 * amount
        if discount >= 200:
            discount == 200
        print("JUMBO Promo_Code", discount)
        amount -= discount

    if promo_code == "BINGO":
        discount = 0.20 * amount
        print("BINGO Promo_Code", discount)
        amount -= 100

    else:
        print("Invalid Promo_code")
else:
    print("You Are Not Eligible To Apply Promo_code")

print("Please Pay \u20b9", amount)

