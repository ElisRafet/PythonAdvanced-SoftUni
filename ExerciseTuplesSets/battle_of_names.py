odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    char_sum = sum(ord(char) for char in input()) // row
    if char_sum % 2 == 0:
        even_set.add(char_sum)
    else:
        odd_set.add(char_sum)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    print(*odd_set.union(even_set), sep=", ")
elif odd_sum > even_sum:
    print(*odd_set.difference(even_set), sep=", ")
elif odd_sum < even_sum:
    print(*odd_set.symmetric_difference(even_set), sep=", ")