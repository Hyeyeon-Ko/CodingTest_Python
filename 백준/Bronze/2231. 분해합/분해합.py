n = int(input())

for i in range(1, n+1):
    #숫자 i의 각 자릿수들의 합
    num = sum((map(int, str(i))))
    num_sum = i + num

    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)