# Given an array of size N-1 containing distinct numbers from 1 to N, find the missing number.

# 📥 Input Format

# First line contains an integer N

# Second line contains N-1 space-separated integers

# 📤 Output Format

# Print the missing number

def missing_number(n,arr):
    actual_sum = n * (n+1) // 2
    cur_sum = sum(arr)
    return actual_sum - cur_sum

n = int(input())
array = list(map(int,input().split()))
print(missing_number(n,array))
