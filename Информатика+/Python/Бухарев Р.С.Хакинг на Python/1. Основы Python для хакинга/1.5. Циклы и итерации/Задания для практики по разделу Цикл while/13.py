word = "python"
guessed = ["_"] * len(word)
attempts = 0

while "_" in guessed:
    letter = input("Введите букву: ")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    print("".join(guessed))
    attempts += 1

print(f"Вы угадали слово за {attempts} попыток!")
