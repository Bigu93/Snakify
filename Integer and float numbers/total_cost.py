a = int(input())
b = int(input())
n = int(input())

m = n * (a + (b / 100))
a1 = int(m)
b1 = round(m % a1, 2)

print(a1)
print(int(100 * b1))
