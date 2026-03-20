# 📝 Problem Statement

# Given an integer N, check whether it is a power of 2 using binary concept.

# 📥 Input

# A single integer N

# 📤 Output

# Print "Yes" if power of 2

# Otherwise print "No"

def is_power_of_two(n):
    if n <= 0 : return "No"
    return "Yes" if (n & (n-1) == 0) else "No"

n = int(input())
print(is_power_of_two(n))