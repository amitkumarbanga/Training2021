# LIST CONTAINER
# square brackets are used in case of lis containers []<<<<<<<<<<<<<<

instagram_id = ["amitbanga0786"]
print("instagram_id:", type(instagram_id))
print("instagram_id is:", hex(id(instagram_id)))

print()

followers = ["jhon", "mike", "jeorge", "loka", "angel", "cristy"]
print("follower:", followers[0])
print("follower:", followers[:3], hex(id(followers[3])))

del followers[2]
print("follower", followers[2])
print("followers now", followers)

print()

print("followers now:", followers)
followers2 = ("simran")
followers1 = ("rohan")

print("followers now:", followers)
followers.append("angel")
print("followers now:", followers)

followers[1] = "divjot"
print("total followers:", len(followers))

print()

