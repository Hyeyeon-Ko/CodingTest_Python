import sys
sys.setrecursionlimit(10 ** 6) # 재귀 사용시 필수! 재귀 깊이 제한 늘려서 런타임에러 없애기 위함.

input = sys.stdin.readline

N, M = map(int, input().split())
result = []
visited = [False] * (N+1) # 중복 허용 x -> 방문했는지 체크하는 리스트 필요

def backtracking(num):
    if num == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtracking(num + 1)

            visited[i] = False
            result.pop()

backtracking(0)