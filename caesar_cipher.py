import string


def translatation(dictionary, word, n):
    answer = ""
    length = len(dictionary)
    for letter in word:
        if letter.isupper():
            new_index = (dictionary.index(letter.lower()) + n) % length
            answer += dictionary[new_index].upper()
        else:
            new_index = (dictionary.index(letter) + n) % length
            answer += dictionary[new_index]
    return answer


english_alphabet = string.ascii_lowercase
russian_alphabet = [chr(i) for i in range(ord('а'), ord('я')+1)]
a = input("Введи слово")
print(russian_alphabet)
print(a)
b = translatation(russian_alphabet, a, 5)
print(b)
