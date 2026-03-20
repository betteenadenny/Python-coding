# 📝 Problem Statement

# Given a binary number, convert it into its decimal equivalent.

# 📥 Input

# A single integer (binary number)

# 📤 Output

# Print the decimal equivalent

def decimal(n):
    power = 0
    decimal = 0

    while(n > 0):
        digit = n % 10
        decimal += digit * (2 ** power)
        power += 1
        n //= 10
    return decimal

n = int(input())
print(decimal(n))
