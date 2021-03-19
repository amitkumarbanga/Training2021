amit_followers = {"divjot", "harjot", "rohan", "simran", "karamveer", "simpreet"}
divjot_followers = {"ramandeep", "riya", "rohan", "amit", "harjot", "karmveer"}
print()
print("<<<<<<<MUTUAL FOLLOWERS OF AMIT AND DIVJOT>>>>>>")
print()

mutual_followers = amit_followers.intersection(divjot_followers)
print("total followers of amit:", amit_followers)
print("total number of amit_followers:", len(amit_followers))
print()

print("total followers of divjot:", divjot_followers)
print("total number of divjot_followers:", len(divjot_followers))
print()

print("MUTUAL FOLLOWERS", mutual_followers)
print("MUTUAL FOLLOWERS", len(mutual_followers))




