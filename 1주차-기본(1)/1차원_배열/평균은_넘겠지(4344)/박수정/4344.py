import sys

c = int(sys.stdin.readline()) # 테스트케이스 갯수

for j in range(c): # 테스트케이스 만큼 반복
    score = list(map(int, sys.stdin.readline().split())) # score[0] = 학생수, 그 뒤로 점수 입력
    
    # 변수 초기화
    sum = 0 # 평균을 구하기 위한 합계
    well = 0 # 평균을 넘는 학생들의 수
    
    # 평균을 구하기 위한 반복
    for i in range(1, score[0]+1): 
        sum += score[i] # score[1] 부터 score[학생수+1] 까지 합계
    avg = sum / score[0] # 평균
    
    # 평균을 넘는 학생 수를 구하기 위한 반복
    for i in range(1, score[0]+1):
        # 평균이 넘는 score[i] : well count
        if score[i] > avg:
            well += 1 
    print("{0:.3f}%".format(well / score[0] * 100)) # 형식에 맞춰 출력
    del score[0:(score[0]+1)] # list 내부 값들을 지우는 del
