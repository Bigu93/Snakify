n = int(input())
m = int(input())

calc = m / n

if calc % 1 != 0:
    calc += 1
    print(int(calc))
else:
    print(calc)
