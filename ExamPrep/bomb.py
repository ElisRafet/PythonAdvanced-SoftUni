rows, cols = map(int, input().split(', '))
matrix = []
c_t = []
for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == "C":
            c_t = [row, col]
            break
time = 16
moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

defused = False
killed = False

while time:
    time -= 1
    command = input()
    if command == 'defuse':
        if matrix[c_t[0]][c_t[1]] != "B":
            time -= 1
        elif matrix[c_t[0]][c_t[1]] == "B":
            time -= 3
            if time >= 0:
                matrix[c_t[0]][c_t[1]] = 'D'
                defused = True
            else:
                matrix[c_t[0]][c_t[1]] = 'X'
            break
    else:
        move = moves[command]
        new_row = c_t[0] + move[0]
        new_col = c_t[1] + move[1]
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if matrix[new_row][new_col] == "T":
                matrix[new_row][new_col] = "*"
                killed = True
                break
            c_t = [new_row, new_col]

if defused:
    print('Counter-terrorist wins!')
    print(f'Bomb has been defused: {time} second/s remaining.')
else:
    print('Terrorists win!')
    if not killed:
        print('Bomb was not defused successfully!')
        print(f'Time needed: {abs(time)} second/s.')

[print(''.join(row)) for row in matrix]