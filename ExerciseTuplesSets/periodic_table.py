elements = set()

# for _ in range(int(input())):
#     for element in input().split():
#         elements.add(element)
#
# for element in elements:
#     print(element)
print(*{element for _ in range(int(input())) for element in input().split()}, sep="\n")