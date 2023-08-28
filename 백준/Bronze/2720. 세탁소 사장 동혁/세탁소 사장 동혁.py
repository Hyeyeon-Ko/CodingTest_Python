changes = [25, 10, 5, 1]
T = int(input())

for _ in range(T):
    C = int(input())
    count = []

    for i in changes:
        count.append(C // i)
        C = C % i

    print(*count)