import sys, math
input = sys.stdin.readline

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n, m = map(int, input().split())

for i in range(n, m+1):
    if is_prime(i):
        print(i)
    else:
        continue