import sys

n=int(sys.stdin.readline()) # 테스트케이스 갯수

for j in range(n): # 테스트케이스만큼 반복
    # O or X를 string 값으로 list에 하나씩 입력
    ox = list(str(sys.stdin.readline())) # ['O', 'X', 'X']
    
    # 변수 초기화
    score = 0 # 점수
    index = 0 # 연속될 경우 추가될 점수
    
    for i in range(len(ox)): # list의 크기만큼 반복
        # O 이면 점수 1점과 연속된 O일 경우 추가점수
        if ox[i] == 'O':
            score += 1+ index
            index += 1 # 다음에도 O이면 이번 추가점수보다 하나 더 큼
        # X 이면 점수 없고 추가점수 초기화됨
        elif ox[i] == 'X' :
            index = 0
        # 예외처리 생략
    print(score, end="\n") # 점수 출력
