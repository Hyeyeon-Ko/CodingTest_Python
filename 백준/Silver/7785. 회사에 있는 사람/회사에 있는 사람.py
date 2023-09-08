import sys
input = sys.stdin.readline

n = int(input())
dict1 = {}

for _ in range(n):
    name, check = map(str, input().split())
    if check == "enter":
        dict1[name] = 1
    else:
        dict1[name] = 0

dict2 = dict(sorted(dict1.items(), reverse=True))

for key, value in dict2.items():
    if value == 1:
        print(key)
    else:
        continue