n = int(input())
n_list = list(map(int, input().split()))

max = max(n_list)
total = 0

for i in range(n):
    total += n_list[i] / max * 100
avg = total / n

print(avg)