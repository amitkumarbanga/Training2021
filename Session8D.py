item = {
    "bat": 2000,
    "football":  2800,
    "golf_kit":  25000,
    "baseball": 1200,
}

item["baseball"] = 1300

item["socks"] = 200

print("Item")
print(item, type(item), hex(id(item)))

print(item["bat"])

equipments = []
cart = []
choice = "yes"
total = 0

while choice == "yes":
    equipment = input('Enter Item:')
    equipments.append(equipment)
    cart.append(item[equipment])
    total += item[equipment]

    choice = input("Enter more item yes/no:")


if sum(cart) > 250:
    print("Complimentary")
   # item.extend(["Bag", "gloves"])
    cart.extend([0, 0])

    print(equipments)
    print(cart)
    print("Amount to pay:", sum(cart))
