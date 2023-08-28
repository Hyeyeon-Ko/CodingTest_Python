T = int(input())
Q = 25
D = 10
N = 5
P = 1

for _ in range(T):
    C = int(input())
    count = []

    if C // Q > 0:
        count.append(C // Q)
        C = C % Q
    else:
        count.append(0)
        
    if C // D > 0:
        count.append(C // D)
        C = C % D
    else:
        count.append(0)

    if C // N > 0:
        count.append(C // N)
        C = C % N
    else:
        count.append(0)

    if C // P > 0:
        count.append(C // P)
    else:
        count.append(0)
    
    for i in count:
        print(i, end=" ")

    print()