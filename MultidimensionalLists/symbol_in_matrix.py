matrix =[]
for _ in range(int(input())):
    row_info = input()
    matrix.append(row_info)

searched_symbol = input()

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == searched_symbol:
            print(f'{row}, {col}')
            exit()

print(f'{searched_symbol} does not occur in the matrix')