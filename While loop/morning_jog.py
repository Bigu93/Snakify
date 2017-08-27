n = int(input())
m = int(input())

k = 1
while n < m:
    n = n + (n * 0.1)
    k += 1

print(k)
