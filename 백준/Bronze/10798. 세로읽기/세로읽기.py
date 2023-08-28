table = [input() for i in range(5)]

for i in range(15):
    for j in range(5):
        
        #입력값의 길이가 전부 다르므로(1~15) 길이에 따라 조건 적용
        if i < len(table[j]):
            print(table[j][i], end="")