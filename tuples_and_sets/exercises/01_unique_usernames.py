n =  int(input())

unique_usernames = set()

for _ in range(n):
    unique_usernames.add(input())

# for name in unique_usernames:
#     print(name)

# print('\n'.join(unique_usernames))
print(*unique_usernames, sep='\n')