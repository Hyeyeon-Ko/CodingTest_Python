#줄별로 리스트 안에 리스트로 입력
board = [[int(x) for x in input().split()] for y in range(9)]

max_list = list(map(max, board))
max_list_index = max_list.index(max(max_list))

for i in range(9):
    if board[max_list_index][i] == max(max_list):
        max_board_index = i

print(max(max_list))
print(max_list_index+1, end=" ")
print(max_board_index+1)