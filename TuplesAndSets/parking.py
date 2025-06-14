n = int(input())
parking = set()

for _ in range(n):
    command, car_number = input().split(", ")
    if command == "IN":
        parking.add(car_number)
    else:
        parking.remove(car_number)

if not parking:
    print('Parking Lot is Empty')
else: print('\n'.join(parking))