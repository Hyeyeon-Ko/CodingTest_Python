croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for a in croatia:
    word = word.replace(a, "*") #word 내의 croatia 리스트에 존재하는 문자열을 *로 바꾸기 

print(len(word))