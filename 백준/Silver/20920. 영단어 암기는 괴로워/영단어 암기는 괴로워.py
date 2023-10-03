import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for _ in range(n):
    word = input().rstrip()

    if len(word) >= m:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

word_lst = sorted(dict.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수

for i in word_lst:
    print(i[0])