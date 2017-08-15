n = int(input())

sum = 1
sum_f = 0

for num in range(1, n + 1):
    sum *= num
    sum_f += sum
print(sum)
