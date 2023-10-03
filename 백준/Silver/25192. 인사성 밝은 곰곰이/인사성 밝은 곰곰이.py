import sys
input = sys.stdin.readline

cnt = 0 # 임티갯수 변수
user = {} # 이름과 임티사용을 확인할 변수

for i in range(int(input().rstrip())): # 채팅방의 기록수만큼 for문을 돌린다
    # 채팅내용입력받음
    s = input().rstrip()
    
    # 새로운 사람이 들어왔을때
    if s == "ENTER":
    	# 이전까지 있었던 임티수를 전부 더한다
        cnt += sum(user.values())
        # dict() 초기화
        user = {}
    else:
    	# 전에 없었던 이름이라면 추가
        if s not in user: 
        	user[s] = 1
        # 전에 있었던 이름이라면 패스

# user에 남아있는 값들도 더해준다.
cnt += sum(user.values())

print(cnt)
