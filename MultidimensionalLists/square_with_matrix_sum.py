rows, cols = map(int, input().split(', '))
matrix = []
mini_matrix_sum = float("-inf")

for _ in range(rows):
    row_info = [int(x) for x in input().split(', ')]
    matrix.append(row_info)

for row_index in range(len(matrix) -1):
    # mini_matrix = []
    for col_index in range(len(matrix[row_index])-1):
        current_el = matrix[row_index][col_index]
        left_el = matrix[row_index][col_index+1]
        bottom_el = matrix[row_index+1][col_index]
        diagonal_el = matrix[row_index+1][col_index+1]
        current_sum = current_el + bottom_el + left_el + diagonal_el
        if current_sum > mini_matrix_sum:
            mini_matrix_sum = current_sum
            mini_matrix = [[current_el, left_el], [bottom_el, diagonal_el]]



print(*mini_matrix[0])
print(*mini_matrix[1])
print(mini_matrix_sum)