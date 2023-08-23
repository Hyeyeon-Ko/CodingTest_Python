N, M = map(int, input().split())
list = []

for a in range(1, N+1):
    list.append(a)

for b in range(M):
    i, j = map(int, input().split())
    list[i-1], list[j-1] = list[j-1], list[i-1]

for c in range(len(list)):
    print(list[c], end=" ")