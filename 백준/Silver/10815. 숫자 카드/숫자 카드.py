import sys
input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))

dict = {}
for i in range(n):
    dict[card_list[i]] = 0 #아무 숫자로 mapping

for j in range(m):
    if check_list[j] in dict:
        print(1, end=" ")
    else:
        print(0, end=" ")