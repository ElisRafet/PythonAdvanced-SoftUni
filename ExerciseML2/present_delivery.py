presents = int(input())
size = int(input())
matrix = []
santa_position = []
nice_kids = 0
nice_kids_gifted = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "S":
            santa_position = [row, col]
        if matrix[row][col] == "V":
            nice_kids += 1

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    row, col = santa_position[0] + directions[command][0], santa_position[1] + directions[command][1]
    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "V":
            nice_kids_gifted += 1
            presents -= 1
            matrix[row][col] = "-"
        elif matrix[row][col] == "C":
            for direction in directions.values():
                next_row, next_col = row + direction[0], col + direction[1]
                if matrix[next_row][next_col] in ["V", "X"] and presents > 0:
                    presents -= 1
                    if matrix[next_row][next_col] == "V":
                        nice_kids_gifted += 1
                    matrix[next_row][next_col] = "-"
        matrix[santa_position[0]][santa_position[1]] = "-"
        santa_position = [row, col]
        matrix[row][col] = "S"

if presents < 1 and nice_kids - nice_kids_gifted > 0:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids - nice_kids_gifted > 0:
    print(f'No presents for {nice_kids - nice_kids_gifted} nice kid/s.')
else:
    print(f'Good job, Santa! {nice_kids_gifted} happy nice kid/s.')