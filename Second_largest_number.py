# Given an array of integers of size N, your task is to find the second largest distinct element in the array.

# If the second largest element does not exist, print -1.

# Input Format

# First line contains an integer N (size of array)

# Second line contains N space-separated integers

# Output Format

# Print a single integer → the second largest element

# If not possible, print -1


import sys
def second_largest(n,arr):
    if(n < 2) or (n != len(arr)):
        return -1
    
    largest = -sys.maxsize
    second_largest = -sys.maxsize

    for i in arr:
        if(i > largest):
            second_largest = largest
            largest = i
        elif(i > second_largest and i != largest):
            second_largest = i
    
    if(second_largest == -sys.maxsize):
        return -1
    else:
        return second_largest

try:    
    n = int(input())
    array = list(map(int,input().split()))
    result = second_largest(n,array)
    print(result)
except ValueError:
    print(-1)