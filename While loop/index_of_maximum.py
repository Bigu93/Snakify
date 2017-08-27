n = 0
temp_max = 0
while True:
    num = int(input())
    n += 1
    if num == 0:
        break
    elif temp_max < num:
        temp_max = num
        max_index = n
print(max_index)
