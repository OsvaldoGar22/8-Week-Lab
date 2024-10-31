# Exercise 1 - Initials
# name = input("Full Name: ")
# names = name.split()
#
# initials = ""
# for n in names:
#     initials += n[0]
#
# print(initials)

# ------------------------------------------------

# Exercise 2 - Sum of Digits in a String
# numbers = input("Enter a bunch of numbers: ")
#
# total_sum = 0
#
# for char in numbers:
#     if '0' <= char <= "9":
#         total_sum += int(char)
# print(total_sum)

# ------------------------------------------------

# Exercise 3 - Date Printer

# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#
# date_input = input("Enter a date in the format mm/dd/yyyy: ") 
# month, day, year = date_input.split('/')
#
# month_name = months[int(month) - 1]
#
# print(f"{month_name} {int(day)}, {year}")

# ------------------------------------------------

# Exercise 4 - Morse Code Converter

# morse_code_dict = {
#     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
#     'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
#     'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
#     'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
#     'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
#     'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
#     '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
#     '7': '--...', '8': '---..', '9': '----.', 
#     '.': '.-.-.-', ',': '--..--', '?': '..--..', 
#     '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-'
# }
#
# text = input("Enter a string: ")
#
# morse_code = " "
#
# for char in text.upper():
#     if char in morse_code_dict:
#         morse_code += morse_code_dict[char] + " "
#     else:
#         morse_code += " "
#
# print(morse_code)

# ------------------------------------------------

# Exercise 5 - Alphabetic Telephone Number Translator

# letter_to_digit = {
#     'A': '2', 'B': '2', 'C': '2',
#     'D': '3', 'E': '3', 'F': '3',
#     'G': '4', 'H': '4', 'I': '4',
#     'J': '5', 'K': '5', 'L': '5',
#     'M': '6', 'N': '6', 'O': '6',
#     'P': '7', 'Q': '7', 'R': '7', 'S': '7',
#     'T': '8', 'U': '8', 'V': '8',
#     'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
# }
#
# phone_number = input("Enter a phone number in the format XXX-XXX-XXXX: ")
#
# converted_number = ""
#
# for char in phone_number:
#     if char.isalpha():
#         converted_number += letter_to_digit[char.upper()]
#     else:
#         converted_number += char
#
# print(converted_number)

# ------------------------------------------------

# Exercise 6 - Average Number of Words

# def average_words(filename):
#     with open(filename, 'r') as file:
#         lines = file.readlines()
#
#     total_words = 0
#     sentence_count = 0
#
#     for line in lines:
#         words = line.split()
#         total_words += len(words)
#         sentence_count += 1
#
#     if sentence_count > 0:
#         average_words = total_words / sentence_count
#     else:
#         average_words = 0
#
#     return average_words
#
# filename = 'text.txt'
# average = average_words(filename)
# print(f"Average number of words per sentence: {average}")

# ------------------------------------------------

# Exercise 7 - Character Analysis

# uppercase_count = 0
# lowercase_count = 0
# digit_count = 0
# whitespace_count = 0
#
# with open('text.txt', 'r') as file:
#     contents = file.read()
#
# for char in contents:
#     if char.isupper():
#         uppercase_count += 1
#     elif char.islower():
#         lowercase_count += 1
#     elif char.isdigit():
#         digit_count += 1
#     elif char.isspace():
#         whitespace_count += 1
#
# print(f"Number of uppercase letters: {uppercase_count}")
# print(f"Number of lowercase letters: {lowercase_count}")
# print(f"Number of digits: {digit_count}")
# print(f"Number of whitespace characters: {whitespace_count}")

# ------------------------------------------------

# Exercise 8 - Sentence Capitalizer 

# def cap_sentences(text):
#     result = ''
#     capitalize_next = True
#     
#     for char in text:
#         if capitalize_next and char.isalpha():
#             result += char.upper()
#             capitalize_next = False
#         else:
#             result += char
#
#         if char == ".":
#             capitalize_next = True
#
#     return result
#
# user_input = input("Write a sentence: ")
#
# modified_text = cap_sentences(user_input)
# print(f"Modified sentence: {modified_text}")

# ------------------------------------------------

# Exercise 9 - Vowels and Consonants

# def main():
#     user_str = input("Enter a string of characters: ")
#
#     print(f"That string has {num_vowels(user_str)} vowels and {num_consonants(user_str)} consonants")
#
# def num_vowels(s):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#
#     v_count = 0
#
#     for ch in s:
#         if ch.lower() in vowels:
#             v_count += 1
#     
#     return v_count
#
# def num_consonants(s):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#
#     c_count = 0
#
#     for ch in s:
#         if ch.isalpha() and ch.lower() not in vowels:
#             c_count += 1
#
#     return c_count
#
# main()

# ------------------------------------------------

# Exercise 10 - Most Frequent Character

def most_character(text):
    freq = {}

    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    most_freq = max(freq, key=freq.get)
    return most_freq

character = input("Enter a sentence: ")

most_freq_character = most_character(character)
print(f"The most frequent character is: {most_freq_character}")




























