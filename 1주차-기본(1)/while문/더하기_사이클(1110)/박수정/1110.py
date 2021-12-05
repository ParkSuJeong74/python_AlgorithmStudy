import sys

n = int(sys.stdin.readline()) # n 입력
tmp = n # tmp를 입력받은 n값으로 초기화
index = 0 # 반복 횟수 초기화

while True:
    a = tmp // 10 # tmp의 10의 자리 숫자
    b = tmp % 10 # tmp의 1의 자리 숫자
    c = (a+b) % 10 # tmp의 10의 자리와 1의 자리의 합 계산 결과의 1의 자리 숫자
    result = (10 * b) + c # 새로운 수
    index += 1 # 반복횟수 카운트
    
    # 새로운 수가 처음 n값과 같으면 반복 탈출
    if result == n: 
        break
    tmp = result # 다음 반복 준비
print(index) # 반복 횟수 카운트 결과
