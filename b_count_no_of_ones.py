# 4. Count Number of 1s in Binary Representation
# 📝 Problem Statement

# Given an integer N, count the number of set bits (1s) in its binary representation.

# 📥 Input

# A single integer N

# 📤 Output

# Print count of 1s

def count_ones(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count

n = int(input())
print(count_ones(n))