# 2. All Unique Strings

# Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.

import random

char_list = ['a', 'e', 'i', 'o', 'I']

random.shuffle(char_list)
print("".join(char_list))

