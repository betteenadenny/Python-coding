n = int(input())
num_bits = n.bit_length()
mask = (1 << num_bits) - 1
result = (n ^ mask)
print(result)