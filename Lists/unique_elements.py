list_n = input().split()
list_n = list(map(int, list_n))

unique = []
for elem in list_n:
    counter = list_n.count(elem)
    if elem not in unique and counter == 1:
        unique.append(elem)

print(unique)
