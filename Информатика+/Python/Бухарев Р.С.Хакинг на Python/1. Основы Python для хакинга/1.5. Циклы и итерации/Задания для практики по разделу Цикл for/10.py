vowels = "aeiouAEIOU"
text = "Hello, World!"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Количество гласных:", count)
