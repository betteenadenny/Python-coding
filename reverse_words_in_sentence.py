# Given a sentence containing multiple words separated by spaces, reverse the order of words in the sentence.

# Do not reverse the letters of the words themselves, only the order of words.

# 📥 Input Format

# A single line containing a sentence S.

# The sentence may contain multiple words separated by spaces.

# Words consist of alphabets (both uppercase and lowercase).

# 📤 Output Format

# Print the sentence with words in reverse order, separated by a single space.

str = input()
str_array = str.split()
str_array.reverse()
print(" ".join(str_array))