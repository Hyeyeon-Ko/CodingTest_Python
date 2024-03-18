import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())

# 1번) 내장 함수 이용
# print(math.gcd(a, b))
# print(math.lcm(a, b))


# 2번) 유클리드 호제법 이용
# 최대공약수
def gcd(a, b):
    while b > 0: 
        a, b = b, a % b 

    return a 

# 최대공배수
def lcd(a, b):
    return (a * b) // gcd(a, b)

print(gcd(a, b))
print(lcd(a, b))