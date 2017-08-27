n = int(input())

a, b = 0, 1
sequence = ''
while a < n:
    sequence += str(a) + ' '
    a, b = b, a+b

if a == n:
    print(len(sequence.split()))
else:
    print(-1)
