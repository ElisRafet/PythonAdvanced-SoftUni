matrix = []
result = 0
for _ in range(int(input())):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

for index in range(len(matrix)):
    result += matrix[index][index]

print(result)