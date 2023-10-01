import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    if a[i] == 0:
        queue.appendleft(b[i])

m = int(input())
arr = list(map(int, input().split()))

for i in arr:
    queue.append(i)
    print(queue.popleft(), end=" ")