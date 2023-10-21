def translatation(dictionary, word, n):
    answer = ""
    length = len(dictionary)
    for letter in word:
        if not (letter.lower() in dictionary):
            answer += letter
            continue
        if letter.isupper():
            new_index = (dictionary.index(letter.lower()) + n) % length
            answer += dictionary[new_index].upper()
        else:
            new_index = (dictionary.index(letter) + n) % length
            answer += dictionary[new_index]
    return answer
