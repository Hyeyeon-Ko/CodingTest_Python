import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
stack = []
target = 1

while num_list:
    if num_list[0] == target:
        num_list.pop(0)
        target += 1
    else:
        stack.append(num_list.pop(0))

    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break

if not stack:
    print("Nice")
else:
    print("Sad")