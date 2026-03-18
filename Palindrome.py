# Given an integer N, check whether it is a palindrome or not.

# A number is said to be a palindrome if it remains the same when its digits are reversed.

# 📥 Input Format

# A single integer N

# 📤 Output Format

# Print "Palindrome" if the number is a palindrome

# Otherwise, print "Not Palindrome"

def palindrome(number):
    actual_number = number
    if number < 0 : return "Not Palindrome"
    rev = 0
    while(number > 0):
        rem = number % 10
        rev = rev * 10 + rem
        number //= 10
    return "Palindrome" if actual_number == rev else "Not Palindrome"

try:
    n = int(input())
    print(palindrome(n))
except ValueError:
    print("Not Palindrome")
