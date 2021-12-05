import sys

n=int(sys.stdin.readline()) # 과목 수 입력
score = list(map(int, sys.stdin.readline().split())) # 점수 입력
sum = 0 # 새로운 점수로 평균을 내기 위한 합계 초기화

for i in range(n):
    # 모든 점수를 점수/M*100로 고친 새로운 점수로 평균을 구해야함
    sum += score[i] / max(score) * 100 # 새로운 값을 sum에 더해줌
print(round((sum / n), 6)) # 평균. 반올림해서 소수점아래 6의 자리까지 출력
