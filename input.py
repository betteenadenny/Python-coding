# length of the array is not given
# 1. Input element in a single line seperated by space
# arr1 = list(map(int,input().split()))
# print(arr1)

# length of the array is given
# 1. Input element the next line
# n = int(input())
# arr2 = []
# for _ in range(n):
#     arr2.append(int(input()))

#input array of array - [[1,2],[3,3],[4,5]]
n1 = int(input())
arr2 = []
for i in range(n1):
    pair = list(map(int,input().split()))
    if len(pair) == 2 :
        arr2.append(pair) 
    
print(arr2)  
 