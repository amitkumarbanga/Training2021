def f(x):
    result = x*x +1
    print("result of f is:", result)

def exp(x):
    result = 2**x
    print("result if exp is:", result)

def add(x, y):
    result = x + y
    print("result if add is:", result)

f(1)
f(2)
f(3)

exp(2)
exp(4)
exp(8)

add(2, 8)
add(11, 19)
add(-11, 19)
add(11, -19)

def apply_promo_code(amount, promo_code):
    if promo_code == "ZOMATO":
        return 0.40*amount
    elif promo_code == "BINGO":
        return 0.50*amount
    else:
        return 0.10*amount

result1 = apply_promo_code(5000, "ZOMATO")
result2 = apply_promo_code(5000, "BINGO")

if result1 > result2:
    print("I Will Use ZOMATO")
else:
    print("I Will Use BINGO")