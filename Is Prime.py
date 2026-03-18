# 📝 Problem Statement

# Given an integer N, determine whether it is a prime number or not.

# A prime number is a number greater than 1 that has no divisors other than 1 and itself.

# 📥 Input Format

# A single integer N

# 📤 Output Format

# Print "Prime" if the number is prime

# Otherwise, print "Not Prime"

def is_prime(number):
    if number <= 1 : return "Not Prime"
    for i in range(2,int((number**0.5))+1):
        if(number % i == 0):
            return "Not Prime"
    return "Prime"

n = int(input())
print(is_prime(n))
    