word = input()

converted_word = ''
for char in word:
    if char.islower():
        converted_word += char.upper()
    else:
        converted_word += char.lower()

print(converted_word)
