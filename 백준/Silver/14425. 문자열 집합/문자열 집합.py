import sys
input = sys.stdin.readline

n, m = map(int, input().split())

check_list = []
for _ in range(n):
    check_list.append(input())

check_dict = {}
for i in check_list:
    check_dict[i] = 1

str_list = []
count = 0
for i in range(m):
    str_list.append(input())
    if str_list[i] in check_dict:
        count += 1
    else:
        continue

print(count)