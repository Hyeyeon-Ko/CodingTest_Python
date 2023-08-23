total = int(input())
total_num = int(input())
sum = 0

for i in range(total_num):
    price, num = map(int, input().split())
    sum += price * num

if total == sum:
    print("Yes")
else:
    print("No")