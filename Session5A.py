# Bubble Sort

data = [22, 15, 68, 40, 1, 6, 70, 55]
print("Data Before:")
print(data)

n = len(data)
for i in range(0, n):

    for j in range(0, n-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
            print("Data Now:")
            print(data)

