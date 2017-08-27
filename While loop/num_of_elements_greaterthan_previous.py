n = 0
k = 0
while True:
    num = int(input())
    if num == 0:
        break
    elif num > n:
        k += 1
    n = num
print(k - 1)
