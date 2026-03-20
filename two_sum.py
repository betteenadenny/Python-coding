# lettcode problem no 167
def two_sum(arr,target):
    seen = {}
    for i,value in enumerate(arr):
        remaining = target - value
        if remaining in seen:
            return [i,seen[remaining]]
        else:
            seen[value] = i

arr = list(map(int,input().split()))
target = int(input())
print(two_sum(arr,target))
