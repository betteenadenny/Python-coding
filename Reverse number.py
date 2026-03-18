# 📝 Problem Statement

# Given an integer N, reverse its digits and print the reversed number.

# If the number is negative, preserve the negative sign.

# 📥 Input Format

# A single integer N

# 📤 Output Format

# Print the reversed integer

def reverse(number):
    is_negative = number < 0
    number = abs(number)
    rev = 0
    while(number > 0):
        reminder = number % 10
        rev = rev * 10 + reminder
        number //= 10
    return -rev if is_negative else rev

try:
    n = int(input())
    result = reverse(n)
    print(result)
except ValueError:
    print(-1)

