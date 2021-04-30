import items as items

state = {
    "active": 15464,
    "confirmed": 45055,
    "deaths":5156,
    "latestupdatedtime": "02/03,2020 21:53:33",
    "state": "maharashtra"
}
# iterating keys value
for key in state:
    # print(key)
    # print(state[key])
    # print(key)`
    print("{} | {}".format(key, state[key]))

for value in state.values():
    print(value)

# tuple
item = state.items()
print(item)

# for item in items:
# print(item[0], item[1]) (not working)

for key, value in state.items():
    print(key, value)