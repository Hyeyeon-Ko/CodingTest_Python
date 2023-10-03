import sys
input = sys.stdin.readline

n = int(input())
dict = {}

dict['ChongChong'] = 1
for _ in range(n):
    a, b = map(str, input().split())
    
    if a == 'ChongChong':
         dict[b] = 1
    elif b == 'ChongChong':
         dict[a] = 1
    else:
        if a in dict:
             dict[b] = 1
        elif b in dict:
             dict[a] = 1

print(len(dict))         