n = int(input())

cars = set()

for _ in range(n):
    direction, number = input().split(", ")
    if direction == "IN":
        cars.add(number)
    elif direction == "OUT":
        cars.remove(number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is empty")