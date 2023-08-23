N, M = map(int, input().split())
list = []

for i in range(1, N+1):
    list.append(i)

for _ in range(M):
    i, j = map(int, input().split())
    temp = list[i-1:j]
    temp.reverse()
    list[i-1:j] = temp

for i in range(N):
    print(list[i], end=" ")