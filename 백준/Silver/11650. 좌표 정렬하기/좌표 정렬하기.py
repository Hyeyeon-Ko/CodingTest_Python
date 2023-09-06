import sys

n = int(input())
point = []

for _ in range(n):
    point.append(list(map(int, sys.stdin.readline().split())))

point.sort()

for i in point:
    print(i[0], i[1])