data = [1, 2, 3, 4, 5, 6]
squared_data = []

for i in range(len(data)):
    squared_data.append(data[i]*data[i])

# List Comprehension's
print("data:", data)
print("squared_data:", squared_data)

squared_data1 = [x**2 for x in data]
cube_data = [x*x*x for x in data]

print("squared_data:", squared_data1)
print("cube_data:", cube_data)

product_price = [121, 653, 656, 545, 512]
discounted_price = [0.5*x for x in product_price]

print("product_price:", product_price)
print("discounted_price:", discounted_price)
