N = int(input())
S = 2
count = 0

for i in range(1, N+1):
    S = S + (S - 1)
    count = S**2
    
print(count) 