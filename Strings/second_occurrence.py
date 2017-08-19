string = input()

first = string.find('f')

if string.count('f') > 1:
    old_part = string[:first+1]
    new_part = string[first+1:]
    print(new_part.find('f') + len(old_part))
elif string.count('f') == 1:
    print('-1')
else:
    print('-2')
