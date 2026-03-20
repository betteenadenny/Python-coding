# 📝 Problem Statement

# Given a decimal number N, convert it into its binary representation.

# 📥 Input

# A single integer N

# 📤 Output

# Print the binary equivalent of N

def binary(n):
    if n == 0: return "0"

    binary = ""
    while n>0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

n = int(input())
print(binary(n))