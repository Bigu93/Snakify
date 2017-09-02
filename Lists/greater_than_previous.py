list_n = input().split()

new_list = []
previous_elem = None
for elem in list_n:
    if type(previous_elem) == int:
        if int(elem) > previous_elem:
            new_list.append(elem)
    previous_elem = int(elem)

print(new_list)
