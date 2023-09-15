import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict_name = {}
dict_num = {}

for i in range(1, n+1):
    name = input().strip()
    dict_name[name] = i
    dict_num[i] = name

for _ in range(m):
    check = input().strip()
    if check.isdigit() == True:
        print(dict_num[int(check)])
    else:
        print(dict_name[(check)])