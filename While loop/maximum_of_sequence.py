n = 0
temp_max = 0
while True:
    num = int(input())
    if num == 0:
        break
    elif temp_max < num:
        temp_max = num

print(temp_max)
