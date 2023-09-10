import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr_1 = set(map(int, input().split()))
arr_2 = set(map(int, input().split()))

print(len(arr_1 - arr_2) + len(arr_2 - arr_1))