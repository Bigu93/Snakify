list_n = input().split()

print([list_n[i] for i in range(len(list_n)) if i % 2 == 0])
