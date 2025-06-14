from collections import deque
n = int(input())
stations_info = deque()
for _ in range(n):
    stat = [int(x) for x in input().split()]
    stations_info.append(stat)
start_position = 0
stops = 0
while stops < n:
    fuel = 0
    for i in range(n):
        fuel += stations_info[i][0]
        distance = stations_info[i][1]
        if distance > fuel:
            stations_info.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)

