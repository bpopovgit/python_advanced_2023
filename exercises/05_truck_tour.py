from collections import deque

number_of_pumps = int(input())

pumps = deque()
start_position = 0
stops_counter = 0

for _ in range(number_of_pumps):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])

while stops_counter < number_of_pumps:
    fuel = 0
    for pump in range(number_of_pumps):
        fuel += pumps[pump][0]
        destination = pumps[pump][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_position += 1
            stops_counter = 0
            break
        else:
            fuel -= destination
            stops_counter += 1

print(start_position)