N, k = map(int, input().split())
N_list = []

for i in range(1, N+1):
    if N % i == 0:
        N_list.append(i)

if k <= len(N_list):
    print(N_list[k-1])
else:
    print("0")