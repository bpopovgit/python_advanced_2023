size = int(input())
directions = input().split(', ')

hazelnuts = 0
squirrel_row = 0
squirrel_col = 0
IS_GAME_OVER = False

matrix = []

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 's':
            squirrel_row = row
            squirrel_col = col

for direction in directions:
    matrix[squirrel_row][squirrel_col] = '*'

    if direction == 'up':
        squirrel_row -= 1
    elif direction == 'down':
        squirrel_row += 1
    elif direction == 'left':
        squirrel_col -= 1
    elif direction == 'right':
        squirrel_col += 1

    if not (0 <= squirrel_row < size and 0 <= squirrel_col < size):
        print("The squirrel is out of the field.")
        IS_GAME_OVER = True
        break
    if matrix[squirrel_row][squirrel_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        IS_GAME_OVER = True
        break
    if matrix[squirrel_row][squirrel_col] == 'h':
        hazelnuts += 1
        if hazelnuts == 3:
            IS_GAME_OVER = True
            print("Good job! You have collected all hazelnuts!")
            break

if not IS_GAME_OVER:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")