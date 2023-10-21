def accommodate_new_pets(capacity, weight_limit, *pets):
    result = []
    pets_mapper = {}

    for pet_type, pet_weight in pets:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if pet_weight > weight_limit:
            continue
        if pet_type not in pets_mapper:
            pets_mapper[pet_type] = 0
        pets_mapper[pet_type] += 1
        capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    [result.append(f"{pet_type}: {pet_count}") for pet_type, pet_count in sorted(pets_mapper.items())]
    # for pet_type, pet_count in sorted(pets_mapper.items()):
    #     result.append(f"{pet_type}: {pet_count}")
    return '\n'.join(result)




print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
