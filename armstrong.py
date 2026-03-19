# 📝 Problem Statement

# Given an integer N, check whether it is an Armstrong number or not.

# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

# 📥 Input Format

# A single integer N

# 📤 Output Format

# Print "Armstrong" if the number is an Armstrong number

# Otherwise, print "Not Armstrong"

def armstrong(n):
    actual_number = n
    length = len(str(n))
    calculated_sum = 0
    while(n > 0):
        rem = n % 10
        calculated_sum += rem ** length
        n = n//10
    return "Armstrong" if calculated_sum == actual_number else "Not Armstrong"

n = int(input())
print(armstrong(n))
