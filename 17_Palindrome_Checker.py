# Q17 - Palindrome Checker
# A palindrome reads the same forward and backward.

text = input("Enter a word or number: ")

reversed_text = text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)

if text.lower() == reversed_text.lower():
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")