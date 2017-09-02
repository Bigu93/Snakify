list_n = input().split()

for i in range(len(list_n)):
    if i + 1 < len(list_n):
        first = int(list_n[i])
        second = int(list_n[i + 1])

        if (first * second) > 0:
            print(first, second)
            break
        else:
            pass
