from collections import deque
substances = [int(x) for x in input().split(', ')]
crystal_energy = deque(int(x) for x in input().split(', '))
potions = []
potions_mapper = {
    110: 'Brew of Immortality',
    100: 'Essence of Resilience',
    90: 'Draught of Wisdom',
    80: 'Potion of Agility',
    70: 'Elixir of Strength'
}

while substances and crystal_energy and potions_mapper:
    current_substance = substances.pop()
    current_energy = crystal_energy.popleft()
    sum_sub_en = current_substance + current_energy
    if sum_sub_en in potions_mapper.keys():
        potions.append(potions_mapper.pop(sum_sub_en))
    else:
        possible_po = [po for po in potions_mapper if po <= sum_sub_en]
        if possible_po:
            next_po = max(possible_po)
            potions.append(potions_mapper.pop(next_po))
            current_energy -= 20
            if current_energy > 0:
                crystal_energy.append(current_energy)
        else:
            current_energy -= 5
            if current_energy > 0:
                crystal_energy.append(current_energy)

if len(potions) == 5:
    print('Success! The alchemist has forged all potions!')
elif len(potions) < 5:
    print("The alchemist failed to complete his quest.")
if potions:
    print(f"Crafted potions: {', '.join(potions)}")
if substances:
    print(f"Substances: {', '.join(map(str, reversed(substances)))}")
if crystal_energy:
    print(f"Crystals: {', '.join(map(str, crystal_energy))}")
