N, B = map(int, input().split())

tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''

while N != 0:
    answer += str(tmp[N % B])
    N = N // B

print(answer[::-1])