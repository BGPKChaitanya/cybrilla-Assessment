# Write a program to find if a string is a palindrome. Print true if the string is a palindrome and print false if it is
# not.

word = input()
word1 = word.lower()
word2 = word1[::-1]
# print(word1)
# print(word2)
if (word1 == word2):
    print("true")
else:
    print("false")