list_n = input().split()
list_n = list(map(int, list_n))

for i in range(0, len(list_n), 2):
    if i + 1 < len(list_n):
        list_n[i], list_n[i+1] = list_n[i+1], list_n[i]

print(list_n)
