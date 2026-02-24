# Q19 - Text Analysis Program
# This program performs different text-related operations.

def count_words(text):
    return len(text.split())

def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

def count_consonants(text):
    return sum(1 for ch in text.lower() if ch.isalpha() and ch not in "aeiou")

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    return "".join(ch for ch in text if ch.lower() not in "aeiou")

def word_frequency(text):
    freq = {}
    words = text.lower().split()
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def longest_word(text):
    words = text.split()
    if words:
        return max(words, key=len)
    return ""


user_text = input("Enter text: ")

print("Word count:", count_words(user_text))
print("Vowel count:", count_vowels(user_text))
print("Consonant count:", count_consonants(user_text))
print("Reversed text:", reverse_text(user_text))
print("Is palindrome:", is_palindrome(user_text))
print("Text without vowels:", remove_vowels(user_text))
print("Longest word:", longest_word(user_text))
print("Word frequency:", word_frequency(user_text))