n_list = []

for _ in range(5):
    n_list.append(int(input()))

print(int(sum(n_list)/5))

n_list.sort()
print(n_list[2])