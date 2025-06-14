n = int(input())
matrix = []
ship = []
moves = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
resource = 100

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            ship = [row, col]
            matrix[row][col] = "."
            break

while True:
    if resource < 5:
        print('Mission failed! The spaceship was stranded in space.')
        break
    resource -= 5
    command = input()
    move = moves[command]
    new_row = ship[0] + move[0]
    new_col = ship[1] + move[1]
    if 0 <= new_row < n or  0 <= new_col < n:
        ship = [new_row, new_col]
        if matrix[new_row][new_col] == "R":
            resource = min(100, resource + 10)
        elif matrix[new_row][new_col] == "M":
            resource -= 5
            matrix[new_row][new_col] = '.'
        elif matrix[new_row][new_col] == "P":
            print(f'Mission accomplished! The spaceship reached Planet B with {resource} resources left.')
            break
    else:
        print('Mission failed! The spaceship was stranded in space.')
        break

if matrix[ship[0]][ship[1]] not in "PR":
    matrix[ship[0]][ship[1]] = "S"

[print(*row) for row in matrix]
