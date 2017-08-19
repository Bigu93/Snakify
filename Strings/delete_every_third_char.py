string = input()

new_string = ""
for char in range(len(string)):
    if char % 3 == 0 or char == 0:
        pass
    else:
        new_string += string[char]

print(new_string)
