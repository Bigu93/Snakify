string = input()

first = string.find('h')
last = string.rfind('h')

frag1 = string[:string.find('h')+1]
frag2 = string[string.rfind('h'):]

reverse_frag = string[first+1:last]
print(frag1 + reverse_frag[::-1] + frag2)
