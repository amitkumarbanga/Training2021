data_june_20 = [23564, 65345, 15454, 54542, 56454]
data_july_19 = [45456, 54544, 54545, 85214, 45412]

print("Max cases in june_20", max(data_june_20))
print("Max cases in july_19", max(data_july_19))
def max_cases(data):
    max = data[0]

    for i in range(1, len(data)):
        if data[i] > max:
            max = data[i]

            print("Max cases for {} is {}:".format(data, max))

            # Re-defined
def max_in_range(data):
    max = data[0]

    for i in range(1, len(data)):
        if data[i] > max:
            max = data[i]

            print("Max cases for {} is {}:".format(data, max))

max_cases(data_june_20)
max_cases(data_july_19)
