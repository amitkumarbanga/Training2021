# TUPLE CONTAINER

"""multivalued containers
tuple
list
set
dictionary
"""
# round brackets used in case of tuple ()<<<<<<<<<<<<<<<<<<

instagram_id = "amitbanga0786"
print("instagram_id:", type(instagram_id))
print("instagram_id is:", hex(id(instagram_id)))

print()

followers = ("toypom", "divraman", "sharohan", "arshimlapuri")
print("followers", type(followers))
print("followers", hex(id(followers)))
print("followeer",followers[0])

print("total follower", len(followers))

print()


# del followers[2] -> this will not work
# tuple doesnt support deletion or updation operations
