numbers = tuple([float(x) for x in input().split()])
num_dict = {}

for num in numbers:
    num_dict[num] = numbers.count(num)

for key, value in num_dict.items():
    print(f'{key:.1f} - {value} times')
