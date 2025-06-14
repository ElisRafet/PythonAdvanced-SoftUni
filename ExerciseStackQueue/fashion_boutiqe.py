clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
used_rack = 0

while clothes:
    used_rack += 1
    current_free_space = rack_capacity
    while clothes and clothes[-1] <= current_free_space:
        current_free_space -= clothes.pop()

print(used_rack)
