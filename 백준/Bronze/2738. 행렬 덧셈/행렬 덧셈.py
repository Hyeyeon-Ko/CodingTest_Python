N, M = map(int, input().split())

#줄별로 리스트 안에 리스트로 입력
board1 = [[int(x) for x in input().split()] for y in range(N)]
board2 = [[int(x) for x in input().split()] for y in range(N)]

for i in range(N):
    for j in range(M):
        print(board1[i][j] + board2[i][j], end=" ")
    print()