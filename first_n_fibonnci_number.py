# 📝 Problem Statement

# Given an integer N, generate and print the first N Fibonacci numbers.

# 📥 Input Format

# A single integer N

# 📤 Output Format

# Print N Fibonacci numbers separated by a space

def fibo(n):
    if n == 1: return [0]
    if n == 2: return [0,1]
    fibo_series = [0,1]
    while(len(fibo_series) < n):
        fibo_series.append(fibo_series[-1] + fibo_series[-2])
    return fibo_series

n = int(input())
result = fibo(n)
for i in result:
    print(i, end=" ")
# print(*result)
# print(*result, sep=",") 
# print(*result, sep="\n") 
