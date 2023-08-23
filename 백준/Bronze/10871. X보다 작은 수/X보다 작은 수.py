n, p = map(int, input().split())
n_list = list(map(int, input().split()))

for i in range(n):
    if n_list[i] < p:
        print(n_list[i], end=" ")