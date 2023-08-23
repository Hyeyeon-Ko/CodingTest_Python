N, M = map(int, input().split())
list = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        list[n-1] = k

for n in range(N):
    print(list[n], end=" ")