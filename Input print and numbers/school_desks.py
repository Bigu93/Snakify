def ceildiv(a, b):
    return -(-a // b)


a = int(input())
b = int(input())
c = int(input())

classes = [a, b, c]
sum = 0

for classroom in classes:
    sum += ceildiv(classroom, 2)

print(sum)
