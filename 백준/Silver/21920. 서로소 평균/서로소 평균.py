import math

n = int(input())
list = list(map(int, input().split()))
x = int(input())

res = 0
cnt = 0

for i in list:
    if math.gcd(i, x) == 1:
        res += i
        cnt += 1

print(round(res/cnt, 6))