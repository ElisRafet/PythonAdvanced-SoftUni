rows = int(input())
matrix = []
for _ in range(rows):
    row_info = [int(x) for x in input().split()]
    matrix.append(row_info)

command = input()
while command != "END":
    command, row, col, value = command.split()
    # row, col, value = int(command[1]), int(command[2]), int(command[3])
    row, col, value = map(int, (row, col, value))
    if command == "Add":
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            matrix[row][col] += value
        else:
            print('Invalid coordinates')
    elif command == "Subtract":
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            matrix[row][col] -=value
        else:
            print('Invalid coordinates')
    command = input()

for row in matrix:
    print(*row)