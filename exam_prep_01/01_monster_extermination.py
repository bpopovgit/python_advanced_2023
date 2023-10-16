from collections import deque

monsters_armor = deque([int(el) for el in input().split(",")])
soldier_strikes_impact = [int(el) for el in input().split(",")]

total_kills = 0

while monsters_armor and soldier_strikes_impact:
    current_monster_defense = monsters_armor.popleft()
    current_soldier_power = soldier_strikes_impact.pop()

    if current_soldier_power >= current_monster_defense:
        total_kills += 1
        current_soldier_power -= current_monster_defense
        if not soldier_strikes_impact and current_soldier_power > 1:
            soldier_strikes_impact.append(current_soldier_power)
        elif soldier_strikes_impact:
            soldier_strikes_impact[-1] += current_soldier_power
    else:
        current_monster_defense -= current_soldier_power
        monsters_armor.append(current_monster_defense)

if not monsters_armor:
    print("All monsters have been killed!")
if not soldier_strikes_impact:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {total_kills}")
