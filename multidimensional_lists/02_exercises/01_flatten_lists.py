strings = input().split("|")

matrix = []

for i in range(len(strings) - 1, -1, -1):   # If there were 3 digits, the last one would be with index 2, we go until 0 (hence the second -1), and the step is -1
    row = [int(x) for x in strings[i].split()]
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, sep=' ', end=' ')