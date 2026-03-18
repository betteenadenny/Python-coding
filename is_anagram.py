# Given two strings S1 and S2, check whether they are anagrams of each other.

# Two strings are said to be anagrams if they contain the same characters with the same frequency, but possibly in a different order.

# 📥 Input Format

# First line → string S1

# Second line → string S2

# 📤 Output Format

# Print "Anagram" if both strings are anagrams

# Otherwise, print "Not Anagram"

def is_anagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if(len(s1) != len(s2)): return "Not Anagram"

    freq = {}
    for chr in s1:
        freq[chr] = freq.get(chr,0) + 1

    for chr in s2:
        if chr not in freq: return "Not Anagram"
        freq[chr] -= 1
        if freq[chr] < 0 : return "Not Anagram"
    return "Anagram"

string1 = input()
string2 = input()
print(is_anagram(string1,string2))