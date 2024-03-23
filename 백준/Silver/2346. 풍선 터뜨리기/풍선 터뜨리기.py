import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque(range(1, int(n+1)))
arr = list(map(int, input().split()))

res = []

while queue:
    num = queue.popleft()
    res.append(num)

    move = arr[num-1]
    if move > 0:
        queue.rotate(-(move-1))
    else:
        queue.rotate(-move)

print(' '.join(map(str,res)))