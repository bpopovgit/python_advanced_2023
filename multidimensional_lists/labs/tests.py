matrix = []

rows_count = 2
cols_count = 3
number = 1

for row_index in range(rows_count):
    matrix.append([])
    for col in range(cols_count):
        matrix[row_index].append(number)
        number += 1

print(matrix[0])
print(matrix[1])

new_matrix = [
    [int(el) for el in input().split(", ")]
    for row_index in range(int(input()))
]

print(new_matrix)