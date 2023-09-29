rows = int(input())
matrix = [[int(x) for x in input().split()]for x in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    row, col, value = int(command[1]), int(command[2]), int(command[3])
    if row < 0 or row >= rows or col < 0 or col >= rows:
        print("Invalid coordinates")
        continue
    if command[0] == 'Add':
        matrix[row][col] += value
    elif command[0] == 'Subtract':
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=' ')