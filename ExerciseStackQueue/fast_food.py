from collections import deque

food_quantity = int(input())
clients = deque(int(x) for x in input().split())
biggest_order = max(clients)
print(biggest_order)

while clients:
    if food_quantity < clients[0]:
        print('Orders left:', *clients)
        break
    else:
        food_quantity -= clients.popleft()

if not clients:
    print('Orders complete')