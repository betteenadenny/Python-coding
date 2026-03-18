# Given two positive integers A and B, find their Greatest Common Divisor (GCD).

# The GCD of two numbers is the largest positive integer that divides both numbers without leaving a remainder.

# 📥 Input Format

# First line contains an integer A

# Second line contains an integer B

# 📤 Output Format

# Print a single integer → the GCD of A and B

# def gcd(a, b):
#     if a < 0 or b < 0: 
#         return 0
#     if b == 0:
#         return a
#     return gcd(b, a % b)
def gcd(a,b):
    if a < 0 or b < 0 : return 0
    while (b != 0):
        a,b = b, a % b  #Euclidean Algorithm
    return a

int1 = int(input())
int2 = int(input())
print(gcd(int1,int2))