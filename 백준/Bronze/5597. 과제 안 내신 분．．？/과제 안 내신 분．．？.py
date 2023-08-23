
list = [i for i in range(1, 31)]
new_list = []

for i in range(28):
    n = int(input())
    new_list.append(n)

final_list = [x for x in list if x not in new_list]
final_list.sort()

for i in range(len(final_list)):
    print(final_list[i])