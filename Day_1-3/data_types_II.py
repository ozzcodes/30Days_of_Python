# ## FORMATTING STRINGS ## #

first_name = 'Tom'
last_name = 'Cruise'
welcome_message = "Welcome" + " " + first_name + " " + last_name
print(welcome_message)  # Welcome Tom Cruise

'''
STRING INDEXES
'''
language = 'python'
first_character = language[0]  # indexing starts from 0
second_character = language[1]
print(first_character)  # p
print(second_character)  # y
# Strings can be manipulated easily with this syntax [start:stop:step-over]
range_1 = language[0:2]  # here it starts from index 0 and ends at index 1
range_2 = language[0::1]  # starts at 0, stops at end with step over 1
range_3 = language[::2]  # starts at 0, till end with step 2
range_4 = language[1:]  # starts at index 1 till end of string
range_5 = language[-1]  # selects last character
range_6 = language[-2]  # second last character
reverse_string = language[::-1]  # starts from end and reverses the string
reverse_string_2 = language[::-2]  # reverses string and skips 1 character

print(range_1)  # py
print(range_2)  # python
print(range_3)  # pto
print(range_4)  # ython
print(range_5)  # n
print(range_6)  # o
print(reverse_string)  # nohtyp
print(reverse_string_2)  # nhy

'''
IMMUTABILITY
'''
favorite_website = 'dev.to'
favorite_website[0] = 'w'
print(favorite_website)  # TypeError: 'str' object does not support item assignment
