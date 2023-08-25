p_list = [1, 1, 2, 2, 2, 8]
num_list = list(map(int, input().split()))

for i in range(len(p_list)):
    p_list[i] = p_list[i] - num_list[i]
    print(p_list[i], end=" ")