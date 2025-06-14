n = int(input())
matrix = []
pacman = []
total_start_count = 0
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
health = 100
freezing = 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "P":
            pacman = [row, col]
            matrix[row][col] = "-"
        elif matrix[row][col] == "*":
            total_start_count += 1

while total_start_count > 0:
    command = input()
    if command == "end":
        break
    move = moves[command]
    new_row = (pacman[0] + move[0]) % n
    new_col = (pacman[1] + move[1]) % n
    if matrix[new_row][new_col] == "*":
        total_start_count -= 1
        matrix[new_row][new_col] = "-"
    elif matrix[new_row][new_col] == "F":
        freezing += 1
        matrix[new_row][new_col] = "-"
    elif matrix[new_row][new_col] == "G":
        if freezing:
            freezing -= 1
        else:
            health -= 50
        if health == 0:
            pacman = [new_row, new_col]
            print(f"Game over! Pacman last coordinates [{pacman[0]},{pacman[1]}]")
            break
        matrix[new_row][new_col] = "-"
    pacman = [new_row, new_col]

if not total_start_count:
    print("Pacman wins! All the stars are collected.")
if total_start_count and health > 0:
    print("Pacman failed to collect all the stars.")
print(f'Health: {health}')
if total_start_count:
    print(f'Uncollected stars: {total_start_count}')
matrix[pacman[0]][pacman[1]] = "P"
[print(''.join(row)) for row in matrix]