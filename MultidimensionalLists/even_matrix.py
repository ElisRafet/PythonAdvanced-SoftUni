matrix = []
sub_matrix = []
for _ in range(int(input())):
    row_info = [int(x) for x in input().split(", ")]
    matrix.append(row_info)

for row_index in range(len(matrix)):
    sub_matrix.append([])
    for el in matrix[row_index]:
        if el % 2 == 0:
            sub_matrix[row_index].append(el)

print(sub_matrix)