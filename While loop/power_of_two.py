n = int(input())

expander = 0
value = 1
while value <= n:
    value = value * 2
    expander += 1

print(expander - 1, value // 2)
