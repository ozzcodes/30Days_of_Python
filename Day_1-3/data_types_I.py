num = 100
print(type(num))  # <class 'int'>

num2 = 99.99
print(type(num2))  # <class 'float>

expression1 = num * 10
print(type(expression1))  # <class 'int'>

expression2 = num + num2
print(type(expression2))  # <class 'float'>

"""
MATH FUNCTIONS
"""
print(round(2.1))  # 2
print(round(5.9))  # 6
print(abs(-34))  # 34

"""
STRINGS
"""
name = 'Python'  # string assignment within single quotes
name2 = "Python"  # string assignment within double quotes
name3 = '''This is a a very long string and supports 
        multiline statements as well'''  # string assignment within 3 single quotes
name4 = 'Hello! \"Rockstar Programmer\"'  # string with escaped character sequence
print(type(name))  # <class 'str'>
print(type(name2))  # <class 'str'>
print(type(name3))  # <class 'str'>
print(type(name4))  # <class 'str'>

first_name = 'Mike'
last_name = 'Tyson'
print(first_name + ' ' + last_name)  # Mike Tyson

'''
user_name = 'John'
age = 40
print(user_name + age)  # TypeError: can only concatenate str (not "int") to str
# This would work in Javscript where it would convert the result to string type
'''

user_name = 'John'
age = 40
print(user_name + str(age))  # John40
print(type(str(age)))

lucky_number = 7
lucky_number_stringified = str(7)
lucky_number_extracted = int(lucky_number_stringified)
print(lucky_number_extracted)  # 7
