word = str(input()).upper()
word_list = list(set(word))
cnt = []

for a in word_list:
    count = word.count(a)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")

else:
    print(word_list[(cnt.index(max(cnt)))])