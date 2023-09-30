import sys, math
input = sys.stdin.readline

n = int(input())

cnt = 0
x = 1

while x*x <= n:
    x += 1
    cnt += 1
print(cnt)