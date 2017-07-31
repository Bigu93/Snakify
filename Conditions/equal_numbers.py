a = int(input())
b = int(input())
c = int(input())

num_list = [a, b, c]

s = []
for i in num_list:
    if i not in s:
        s.append(i)

if len(s) == 1:
    print(3)
elif len(s) == 2:
    print(2)
else:
    print(0)
