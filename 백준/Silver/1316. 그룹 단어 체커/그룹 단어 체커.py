N = int(input())
check_list = []
cnt = 0

for _ in range(N):
    word = list(input())
    check_list.append(word[0])
    check = True

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        else:
            if check_list.count(word[i+1]) == 0:
                check_list.append(word[i+1])
            else:
                check = False

    if check == True:
        cnt += 1
        check_list = []
    else:
        check_list = []

print(cnt)