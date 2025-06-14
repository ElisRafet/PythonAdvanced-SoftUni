matrix = []
my_position = []
targets = 0
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
target_down = []

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == "A":
            my_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

for _ in range(int(input())):
    command = input().split()
    move = directions[command[1]]
    if command[0] == "move":
        row = my_position[0] + move[0] * int(command[2])
        col = my_position[1] + move[1] * int(command[2])
        if 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] == ".":
            matrix[row][col] = "A"
            matrix[my_position[0]][my_position[1]] = "."
            my_position = [row, col]
    elif command[0] == "shoot":
        row = my_position[0] + move[0]
        col = my_position[1] + move[1]
        while 0 <= row < 5 and 0 <= col < 5:
            if matrix[row][col] == "x":
                matrix[row][col] = "."
                targets -= 1
                target_down.append([row, col])
                break
            row += move[0]
            col += move[1]
        if targets <= 0:
            print(f"Training completed! All {len(target_down)} targets hit.")
            break

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(row) for row in target_down]