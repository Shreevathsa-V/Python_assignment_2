# Q3 - String Manipulator
# This program analyzes a given sentence.

sentence = input("Enter a sentence: ")

# Basic analysis
print("\nOriginal sentence:", sentence)
print("Total characters (with spaces):", len(sentence))
print("Total characters (without spaces):", len(sentence.replace(" ", "")))

# Splitting sentence into words
words = sentence.split()

print("Total words:", len(words))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())

# Checking if list is not empty before accessing elements
if words:
    print("First word:", words[0])
    print("Last word:", words[-1])

# Reversing entire sentence using slicing
print("Reversed sentence:", sentence[::-1])