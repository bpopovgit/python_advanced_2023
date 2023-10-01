def nums_sums(*args):
    negatives_sum = 0
    positives_sum = 0
    for num in args:
        if num > 0:
            positives_sum += num
        else:
            negatives_sum += num
    # negative_sum = [x for x in args if x < 0]
    # positive_sum = [x for x in args if x > 0]

    return negatives_sum, positives_sum


nums = [int(x) for x in input().split()]

print(nums_sums(*nums)[0])
print(nums_sums(*nums)[1])
if abs(nums_sums(*nums)[0]) > nums_sums(*nums)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")