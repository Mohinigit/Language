string = 'Python'
print(string)

string = "Python"
print(string)

string = '''Python Language'''
print(string)

string = """Guido
 Van
 Rossum"""
print(string)

print('\n')

string_o = "Rakshita has a great "
string_t = "fashion sense"
print(string_o + string_t)

print('\n')

var = "Michael is excellent in coding"
print(len(var))

my_string = "FullStack"
print(my_string[4:])
print(my_string[2:7])
print(my_string[:4])
print(my_string[:])

print('\n')

string = "Full Stack Developer"
res = string.index("Stack")
print(res)

print('\n')

import re
substr = "Madira"
str = "Madira is harmful"
print(re.match(substr,str))

print('\n')

str = "Geeks"
str1 = "geeks"
str2 = str
print(str == str1)
print(str != str1)
print(str == str2)
print(str2 == str1)

print('\n')

text = "Welcome to Wonderland"
print(text.startswith("Welcome"))
print(text.startswith("Wonder",11,17))
print(text.startswith("to",0,11))
print(text.endswith("land"))

print('\n')

str = "general"
print(id(str))

str1 = "general"
print(id(str1))

str2 = "general!"
print(id(str2))

print(str == str1)
print(str1 == str2)
print(str == str2)
print(str1 != str2)
print(str != str2)
print(str is str1)
print(str1 is not str2)

print('\n')

str_1 = "  Freelance developer  "
print(str_1.strip())
print(str_1.lstrip())
print(str_1.rstrip())

print(str_1.replace("Freelance","Python"))

print(str_1.replace('e','a'))

print('\n')

str_1 = "Full-Stack-Developer"
print(str_1.split("-"))

print('\n')

num = 7.0
print("The datatype of number is",type(num))
converted_num = f'{num}'
print(type(converted_num))

print('\n')

str_1 = "geeKs For Geeks"
print(str_1.upper())
print(str_1.lower())






