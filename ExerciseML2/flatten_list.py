string_list = input().split("|")
matrix = []

while string_list:
    row = string_list[-1].split()
    matrix.append(row)
    string_list.pop()

for row in matrix:
    print(*row, end=" ")