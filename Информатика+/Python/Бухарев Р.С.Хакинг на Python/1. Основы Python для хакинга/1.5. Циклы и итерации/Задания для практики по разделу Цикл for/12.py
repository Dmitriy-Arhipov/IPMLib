text = "abcdef"
substring_length = 3
substrings = []
for i in range(len(text) - substring_length + 1):
    substrings.append(text[i:i+substring_length])
print("Подстроки:", substrings)
