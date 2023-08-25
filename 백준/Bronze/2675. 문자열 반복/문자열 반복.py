T = int(input())

for _ in range(T):
    n, S = input().split()
    
    for i in S:
        print(i * int(n), end="")
    print()