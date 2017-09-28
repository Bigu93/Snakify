coordinates = []

while len(coordinates) < 8:
    n = input().split()
    coordinates.append(n)

coordinates = [[int(j) for j in i] for i in coordinates]
coordinates_copy = coordinates[:]

yes_and_no = []
for i, x in enumerate(coordinates):
    for j, y in enumerate(coordinates_copy):
        if ((abs(x[0] - y[0]) == abs(x[1] - y[1])) or
                (x[0] == y[0]) or (x[1] == y[1])) and (i != j):
            yes_and_no.append("YES")
        else:
            yes_and_no.append("NO")

if yes_and_no.count("YES") > 1:
    print("YES")
else:
    print("NO")
