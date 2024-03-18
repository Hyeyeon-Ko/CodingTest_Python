import sys

input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))
result = 1

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

for i in arr:
    if is_prime(i):
        result *= i

print(result if result != 1 else -1)