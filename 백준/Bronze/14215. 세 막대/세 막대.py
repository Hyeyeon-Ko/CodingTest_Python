len_list = list(map(int, input().split()))
k = sum(len_list) - max(len_list)

if k <= max(len_list):
    print(2*k - 1)
else:
    print(sum(len_list))