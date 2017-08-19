string = input()

first = string.find('h')
last = string.rfind('h')

new_string = ""
for char in range(len(string)):
    if (char == string.find('h') or
            char == string.rfind('h')):
        new_string += string[char]
    elif string[char] == 'h':
        new_string += string[char].capitalize()
    else:
        new_string += string[char]

print(new_string)
