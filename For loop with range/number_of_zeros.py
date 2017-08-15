num_of_nums = int(input())
numbers = [int(input()) for i in range(num_of_nums)]

zeros = 0
for i in numbers:
    if i == 0:
        zeros += 1

print(zeros)
