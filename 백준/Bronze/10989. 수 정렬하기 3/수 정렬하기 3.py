import sys

n = int(input())
num = [0 for i in range(10001)]

for i in range(n):
    a = int(sys.stdin.readline())
    num[a] += 1

for i in range(1, 10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)