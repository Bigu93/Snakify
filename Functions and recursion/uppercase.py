text = input()


def capitalize(lower_case_word):
    return ' '.join(word[0].upper() + word[1:]
                    for word in lower_case_word.split())


print(capitalize(text))
