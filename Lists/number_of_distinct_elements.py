list_n = input().split()
list_n = list(map(int, list_n))

count = []
count_num = []
for elem in list_n:
    if elem not in count_num:
        count.append(list_n.count(elem))
        count_num.append(elem)

print(len(count))
