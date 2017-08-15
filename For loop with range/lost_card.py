num_of_nums = int(input())
range_list = list(range(1, num_of_nums + 1))

items = []
for i in range(1, num_of_nums):
    number = int(input())
    items.append(number)

result = list(set(range_list) - set(items))
print(result[0])
