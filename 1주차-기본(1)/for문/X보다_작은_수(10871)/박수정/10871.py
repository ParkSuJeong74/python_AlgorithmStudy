import sys

n, x = map(int, sys.stdin.readline().split()) # N과 X 입력
a = list(map(int, sys.stdin.readline().split())) # 수열 A를 이루는 정수 N개, list 형태로 입력

for i in range(n): # n은 list a의 크기
    # A에서 X보다 작은 수 출력
    if a[i] < x:
        print(a[i], end=" ")
