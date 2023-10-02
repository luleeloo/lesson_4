# task 1
# string = input("Enter a string of characters: ")
#
# letter_count = 0
# digit_count = 0
#
# for chr in string:
#     if chr.isalpha():
#         letter_count += 1
#     elif chr.isdigit():
#         digit_count += 1
# print("Number of letters in the string:", letter_count)
# print("Number of digits in the string:", digit_count)

# task 2
# string = input("Enter a string of characters: ")
# search_chr = input("Enter the character you want to find in the string: ")
#
# count = 0
#
# for chr in string:
#     if chr == search_chr:
#         count += 1
#         print(f"The character has been located {count} time(s)")
#     else:
#         print("The character has not been found")
#         break

# task 3
# try:
#     string = input("Enter a string of characters: ")
#     old_word = input("Enter the word you would like to have replaced: ")
#     if string.find(old_word) == -1:
#         print(f"No such a word in the string!")
#     else:
#         new_word = input("Enter the new word for replacement: ")
#         copy_string = string.replace(old_word, new_word)
#         print(f"Result: {copy_string}")
# except Exception as e:
#     print(f"Something went wrong: {e}")

# task 4
# string = ("Sunlight is made up of many wavelengths—or colors—of light.")
# print(string[2])
# print(string[-2])
# print(string[:5])
# print(string[:-2])
# print(string[::2])
# print(string[1::2])
# print(string[::-1])
# print(string[::-2])
# print(len(string))

# all main tasks finished