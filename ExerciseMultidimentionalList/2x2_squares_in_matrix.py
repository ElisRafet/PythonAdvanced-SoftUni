rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]
counter = 0
for row_index in range(len(matrix) -1):
    for col_index in range(len(matrix[row_index]) - 1):
        current_symbol = matrix[row_index][col_index]
        left_symbol = matrix[row_index][col_index + 1]
        bottom_symbol = matrix[row_index + 1][col_index]
        diagonal_symbol = matrix[row_index + 1][col_index + 1]
        if current_symbol == left_symbol == bottom_symbol == diagonal_symbol:
            counter += 1

print(counter)