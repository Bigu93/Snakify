n = 0
temp_max = 0
while True:
    num = int(input())
    if num == 0:
        break
    elif temp_max < num:
        temp_max = num
    elif temp_max == num:
        n += 1
print(n + 1)
