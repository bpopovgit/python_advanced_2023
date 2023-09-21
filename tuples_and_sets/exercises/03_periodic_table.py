n = int(input())

unique_chemical_elements = set()

for _ in range(n):
    elements = input().split()
    for element in elements:
        unique_chemical_elements.add(element)

print(*unique_chemical_elements, sep='\n')