list_n = input().split()

max_value = ""
for i in range(len(list_n)):
    if i + 1 < len(list_n):
        a = list_n[i]
        b = list_n[i + 1]
        if a > max_value:
            max_value = a
        if b > max_value:
            max_value = b


print(max_value, list_n.index(max_value))
