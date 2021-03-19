# Bitwise Operators
# & | ^

# Shift Operators
# <<, >>

# mostly used in gaming, networking more so on

num1 = 12
num2 = 4

print(bin(num1 & num2))
print(bin(num2 & num1 ))

num3 = num1 & num2
print(num3, bin(num3))

num4 = num1 ^ num2
print(num4, bin(num4))
print(num1, num2)

# Bitwise XOR
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print(num1, num2)

num1 = 12
num6 = num1 >> 2
print(bin(num6))

num7 = num1 << 2
print(bin(num7))

data = 8
key = 2

sent_info = data >> key
print("sent_info is:", sent_info)

receive_info = sent_info << key
print("received_info", receive_info)



