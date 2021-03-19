# SET
# Curly Brackets Are Used In Case Of SET

name1 = "amit"
name2 = "banga"

print(name1, type(name1), hex(id(name1)))
print(name2, type(name2), hex(id(name2)))

followers = {"jhon", "mike", "jeorge", "loka", "angel", "cristy"}

print("total followers:", len(followers))

followers.add("bobby")
followers.add("ak")
print("followers now:", followers)
print()

print("AFTER ADDING 2 FOLLOWERS")

print()

print("followers now:", followers)

print()

print("AFTER REMOVING mike")
print("total followers:", len(followers))

print()

followers.remove("mike")
print("followers now:", followers)

print("followers now:", len(followers))

