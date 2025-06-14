rows, cols = map(int, input().split(", "))
matrix = []
sum_of_matrix = 0

for _ in range(rows):
    row_data =[int(x) for x in input().split(", ")]
    sum_of_matrix += sum(row_data)
    matrix.append(row_data)

print(sum_of_matrix)
print(matrix)