from collections import deque

kids = deque(input().split())
n = int(input()) - 1

while (len(kids)) > 1:
    kids.rotate(-n)
    removed_kids = kids.popleft()
    print(f"Removed {removed_kids}")

print(f'Last is {kids[0]}')