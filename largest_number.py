# Given an array of integers of size N, find the largest element in the array.

# 📥 Input Format

# First line contains an integer N

# Second line contains N space-separated integers

# 📤 Output Format

# Print a single integer → the largest element

# 🔒 Constraints

# 1 ≤ N ≤ 10^5

# -10^9 ≤ array[i] ≤ 10^9
def largest_num(arr):
    largest_num = arr[0]
    for i in arr:
        if i > largest_num:
            largest_num = i
    return largest_num

n = int(input())
array = list(map(int,input().split()))
print(largest_num(array))
    