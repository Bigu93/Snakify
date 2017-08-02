a = int(input())
b = int(input())
c = int(input())

num_list = [a, b, c]

num_dict = {i: num_list.count(i) for i in num_list}

for value in num_dict.values():
    if value > 1:
        print(value)
        break
    else:
        print(0)
        break
