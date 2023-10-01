import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
round = deque(range(1, n+1))
result = []

while round:
    for _ in range(k-1):
        round.rotate(-1)
    result.append(round.popleft())

print("<", end = "")
print(', '.join(map(str, result)), end="")
print(">")