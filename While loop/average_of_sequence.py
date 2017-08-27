n = 0
k = 0
while True:
    num = int(input())
    if num == 0:
        break
    else:
        n += num
        k += 1

print(n / k)
