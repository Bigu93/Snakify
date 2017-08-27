n = int(input())

a, b = 0, 1
i = 1
while i in range(n + 1):
    a, b = b, a+b
    i = i + 1
print(a)
