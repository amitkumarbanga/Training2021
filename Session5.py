from Session2B import name

start_floor = 1
total_floor = 10
my_floor  = int(input("What's your floor number:"))

for floor in range(start_floor, total_floor+1):
    print("elevator has reached floor #{}".format(floor))
    if floor == my_floor:
        print("floor reached please get down!")
        break

num = 5
for i in range(1, 11):
    if i<5:
        continue

print("{} {}'s are #{}".format(num, i, num*1))

drivers = [
        {
            "name": "amit",
            "status": 0,
            "distance": 5
        },
       {
            "name": "divjot",
            "status": 1,
            "distance": 3
       },
       {
            "name": "harjot",
            "status": 1,
            "distance": 15
       },
       {
            "name": "rohan",
            "status": 1,
            "distance": 4
       },
       {
            "name": "simran",
            "status": 1,
            "distance": 9
       }
    ]

customer = {
            "name": "amit",
            "email": "amit123@gmail.com",
            "phone": "6356552333",
            "distance": 5
}

for i in range(len(drivers)):
    if drivers[i]["status"] != 1 and drivers[i]["distance"] > 5:
        continue

    print('Driver Found and Detail Send:', [i], ["name"])
    print("Dear", customer["name"], "your cab booked: SMS sent on: ", customer["phone"])
    print("Dear", customer["name"], "your cab booked: Email sent on: ", customer["email"])
    drivers[i]["status"] = 0
    break


