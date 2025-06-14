matrix = []

for row_index in range(int(input())):
    row_data = [int(x) for x in input().split(', ')]
    matrix.append(row_data)

result = []

for row in matrix:
    for element in row:
        result.append(element)

print(result)