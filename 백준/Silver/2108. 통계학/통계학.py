import sys
import math
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    arr.append(num)

arr.sort()

# 산술평균
print(round(sum(arr) / n))

# 중앙값
print(arr[n // 2])

# 최빈값
cnt = Counter(arr).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

# 범위
print(arr[-1] - arr[0])