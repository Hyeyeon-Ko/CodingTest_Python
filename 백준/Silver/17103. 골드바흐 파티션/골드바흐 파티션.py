import sys, math
input = sys.stdin.readline

#소수 골라내기 (에라토스테네스의 체 활용)
primeNum = [False, False] + [True]*999999

for i in range(2, 1000001):
    if primeNum[i]:
        for j in range(i*2, 1000001, i):
            primeNum[j] = False

t = int(input())

#문제 풀이
for i in range(t):
    count = 0
    n = int(input())
    for j in range(2, n//2+1):
        if primeNum[j] and primeNum[n-j]:
            count += 1
    print(count)