from collections import deque
water_quantity = int(input())
name = input()
queue = deque()

while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) == 1:
        liters_to_serve = int(data[0])
        person_name = queue.popleft()
        if water_quantity >= liters_to_serve:
            print(f"{person_name} got water" )
            water_quantity -= liters_to_serve
        else:
            print(f"{person_name} must wait")
    else:
        liters_to_fill = int(data[1])
        water_quantity += liters_to_fill

    command = input()

print(f"{water_quantity} liters left")