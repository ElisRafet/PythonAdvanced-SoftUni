rows, cols = map(int, input().split(', '))
matrix = []

for _ in range(rows):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

for col_index in range(cols):
    col_sum = 0
    for row_index in range(rows):
        col_sum += matrix[row_index][col_index]
    print(col_sum)