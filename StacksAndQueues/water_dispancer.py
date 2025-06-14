from collections import deque

liters = int(input())
people = deque()
name = input()

while name != "Start":
    people.append(name)
    name = input()

command = input()
while command != "End":
    if command.startswith("refill"):
        _, add_liters = command.split()
        liters += int(add_liters)
    else:
        name = people.popleft()
        wanted_liters = int(command)
        if wanted_liters <= liters:
            print(f'{name} got water')
            liters -= wanted_liters
        else:
            print(f'{name} must wait')
        command = input()

print(f"{liters} liters left")