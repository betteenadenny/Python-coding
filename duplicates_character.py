# Given a string S, find all characters that appear more than once in the string.

# Count the number of times each character appears.

# Return or print only the duplicate characters along with their frequency.

# 📥 Input Format

# A single line containing the string S

# 📤 Output Format

# Print each duplicate character along with its count

# You can print in order of first appearance or sorted order, depending on requirement

# 🔒 Constraints

# 1 ≤ length of S ≤ 10^5

def count_duplicates(string):
    fre = {}
    for ch in string:
        fre[ch] = fre.get(ch,0) + 1
    return fre

str = input()
result = count_duplicates(str)
for i in result.keys():
    if result[i] > 1:
        print(i, result[i])


