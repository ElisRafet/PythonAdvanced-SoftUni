from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque(int(x) for x in input().split())
total_goals = 0

while strength and accuracy:
    current_sum = strength[-1] + accuracy[0]
    if current_sum == 100:
        strength.pop()
        accuracy.popleft()
        total_goals += 1
    elif current_sum < 100:
        if strength[-1] < accuracy[0]:
            strength.pop()
        elif strength[-1] > accuracy[0]:
            accuracy.popleft()
        else:
            strength[-1] += strength[-1]
            accuracy.popleft()
    elif current_sum > 100:
        strength[-1] -= 10
        accuracy.rotate(-1)

if total_goals == 3:
    print("Paul scored a hat-trick!")
elif total_goals == 0:
    print("Paul failed to score a single goal.")
elif total_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < total_goals < 3:
    print("Paul failed to make a hat-trick.")
if total_goals:
    print(f'Goals scored: {total_goals}')

if strength:
    print(f'Strength values left: {", ".join(str(x) for x in strength)}')
if accuracy:
    print(f'Accuracy values left: {", ".join(str(x) for x in accuracy)}')