string = input("Введите строку: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"Символ '{char}' встречается {count} раз(а)")
