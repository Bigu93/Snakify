string = input()
len_s = len(string)

half = len_s - (len_s // 2)
print(string[half:] + string[:half])
