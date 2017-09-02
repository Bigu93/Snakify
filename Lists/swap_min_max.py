list_n = input().split()
list_n = list(map(int, list_n))

max_n = max(list_n)
min_n = min(list_n)

min_index = list_n.index(min_n)
max_index = list_n.index(max_n)

list_n[min_index] = max_n
list_n[max_index] = min_n

print(list_n)
