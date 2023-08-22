F, S, T = map(int, input().split())

if F == S and S == T:
    print(10000+F*1000)
else:
    if F == S:
        print(1000+F*100)
    elif S == T:
        print(1000+S*100)
    elif T == F:
        print(1000+T*100)
    else:
        if F > S and F > T:
            print(F*100)
        elif S > F and S > T:
            print(S*100)
        else:
            print(T*100)