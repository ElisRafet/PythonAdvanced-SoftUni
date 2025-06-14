n = int(input())
reservations = set()

for _ in range(n):
    reservation = input()
    reservations.add(reservation)

guest = input()
while guest != "END":
    reservations.remove(guest)
    guest = input()

print(len(reservations))
for guest in sorted(reservations):
    print(guest)