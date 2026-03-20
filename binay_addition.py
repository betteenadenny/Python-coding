# 📝 Problem Statement

# Given two binary numbers, add them and print the result in binary.

# 📥 Input

# First line → binary number A

# Second line → binary number B

# 📤 Output

# Print the binary sum

def add_binary(a,b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0 or carry:
        sum_val = carry

        if i >= 0:
            sum_val += int(a[i])
            i -= 1
        
        if j >= 0:
            sum_val += int(b[j])
            j -= 1
 
        result = str(sum_val % 2) + result
        carry = sum_val // 2
    return result

a = input()
b = input()
print(add_binary(a,b))
