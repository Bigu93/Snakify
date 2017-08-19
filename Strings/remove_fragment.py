string = input()

first = string.find('h')
last = string.rfind('h')

new_string = string[:first] + string[last+1:]
print(new_string)
