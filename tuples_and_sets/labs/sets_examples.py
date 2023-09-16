a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
intersection = a & b
subset = a < b
diff = a - b
sym_diff = a ^ b
print(union) # print(a.union(b))
print(intersection) # print(a.intersection(b))
print(subset) # print(a.issubset(b))
print(diff) # print(a.difference(b))
print(sym_diff) # print(a.symmetric_difference(b))

