# 📝 Problem Statement

# Given an integer N, your task is to count the number of digits in the number.

# 📥 Input Format

# A single integer N

# 📤 Output Format

# Print a single integer → number of digits in N

def count(number):
    number = abs(number)
    if number == 0 : return 1
    count = 0
    while(number > 0):
        number //= 10
        count += 1
    return count

try:
    n = int(input())
    print(count(n))
except ValueError:
    print(-1)