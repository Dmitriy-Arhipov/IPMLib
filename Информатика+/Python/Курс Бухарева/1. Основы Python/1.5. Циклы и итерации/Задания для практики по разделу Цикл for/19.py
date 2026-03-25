strings = ['hello', 'world', 'hi', 'Python']
min_length = 3
long_strings = []
for string in strings:
    if len(string) > min_length:
        long_strings.append(string)
print("Строки длиной более 3 символов:", long_strings)
