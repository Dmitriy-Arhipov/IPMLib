import string as strlib

def is_palindrome(s):
    s = s.lower()
    s = ''.join([char for char in s if char not in strlib.punctuation and char != " "])
    return s == s[::-1]

input_string = input("Введите строку: ")
if is_palindrome(input_string):
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
