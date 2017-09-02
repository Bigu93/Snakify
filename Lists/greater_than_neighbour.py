list_n = input().split()

counter = 0
for i in range(len(list_n)):
    if i + 1 < len(list_n) and i - 1 >= 0:
        a = list_n[i - 1]
        b = list_n[i + 1]
        num = list_n[i]
        if num > a and num > b:
            counter += 1

print(counter)
