# 📝 Problem Statement

# Given a sorted array of integers, remove the duplicates in-place such that each element appears only once. Return the new length of the array.

# You are not allowed to use extra array for storing results. Modify the input array in-place.

# 📥 Input Format

# First line contains an integer N → size of the array

# Second line contains N space-separated integers → the elements of the array

# 📤 Output Format

# Print a single integer → the new length of the array after removing duplicates

def remove_duplicates(arr):
    if not arr:
        return 0
    
    j = 0 #tracking the index of unique element

    for i in range(1,len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return j+1


n = int(input())
array = list(map(int, input().split()))
print(remove_duplicates(array))