string = input()

first = string.find('f')
last = string.rfind('f')

if string.count('f') > 1:
    print(first, last)
elif string.count('f') == 1:
    print(first)
else:
    pass
