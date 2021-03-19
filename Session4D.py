maharashtra = 52365
delhi = 15466
mumbai = 15455
chandigarh = 45452
jalandhar = 21541

total_cases = maharashtra + delhi + mumbai + chandigarh + jalandhar

print(total_cases)

states = [52365 + 15466 + 15455 + 45452 + 21541]

i = 0
total_cases = 0

while i < 5:
    total_cases += states[i]
    i+=1

print(total_cases)