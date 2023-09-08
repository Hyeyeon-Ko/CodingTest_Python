import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
dict1 = {}

for i in card:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

m = int(input())
check = list(map(int, input().split()))

for i in check:
    result = dict1.get(i)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")