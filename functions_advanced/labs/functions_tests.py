def sum_nums(a, b, *args):
    return args


# print(sum_nums(5, 6, 7))
# print(sum_nums(1, 2))
# print(sum_nums(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def example_function(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#     return kwargs
#
# print(example_function(num=5, name="Peter", id=2))


my_dict = {'Peter': 21, 'George': 18, 'John': 45}

sorted_dict = sorted(my_dict.items(), key=lambda kvp: kvp[1])

for kvp in sorted_dict:
    print(kvp)