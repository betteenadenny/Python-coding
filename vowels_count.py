# 📥 Input Format

# A single line containing a string S

# 📤 Output Format

# Print two integers separated by space:
# 👉 number of vowels and number of consonants

# 🔒 Constraints

# 1 ≤ length of S ≤ 10^5

# String contains only alphabets (uppercase & lowercase)

def count(string):
    string = string.lower()
    vowels = {'a',"e","i","o","u"}
    vowel_count = 0
    consonants_count = 0
    for i in string:
        if i in vowels:
            vowel_count += 1
        else:
            consonants_count += 1
    return vowel_count,consonants_count

string = input()
v,c = count(string)
print(v,c)