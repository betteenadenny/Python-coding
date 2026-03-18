# Given an array of integers of size N, count the frequency of each element and print them in ascending order of elements.

# 📥 Input Format

# First line contains an integer N

# Second line contains N space-separated integers

# 📤 Output Format

# For each distinct element, print:

# element frequency

# Each element-frequency pair should be on a new line

# Elements must be in ascending order
from collections import Counter
def count_freq(arr):
    fre = {}
    for i in arr:
        fre[i] = fre.get(i,0) + 1
    return fre

n = int(input())
array = list(map(int,input().split()))
result = Counter(array)
# result = count_freq(array)
for i in sorted(result.keys()):
    print(i, result[i])
