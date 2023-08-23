n = int(input())
n_list = list(map(int, input().split()))
p = int(input())
count = 0

for i in range(n):
    if n_list[i] == p:
        count += 1
    
print(count)