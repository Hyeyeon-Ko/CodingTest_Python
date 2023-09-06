n = int(input())
word = []

for _ in range(n):
    word.append(input())

word = list(set(word)) #중복된 단어는 하나만 남기고 제거
word.sort(key=lambda x: (len(x), x)) #길이순 오름차순 후, 사전 순 정렬

for i in word:
    print(i)