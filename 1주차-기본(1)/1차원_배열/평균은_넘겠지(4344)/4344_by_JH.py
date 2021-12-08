n=int(input())             #테스트 케이스
hab=0              #평균에 쓸 변수
lenth=0              #테스트 케이스 마다 받을 리스트의 길이
count=0               
for i in range(n):           #테스트 케이스 시작
    count=0
    score=list(map(int,input().split()))               #리스트 받음 (여기서 5 50 50 70 80 100 을 한 리스트에 저장 [0]인덱스의 값:5 가 학생 수이다.)
    lenth=len(score)                                     #리스트 길이
    average=(sum(score)-score[0])/(lenth-1)                 #평균 구하는 법:{리스트합계 에서 [0]인덱스의 값을 뺀 값(점수총합)} / {리스트 길이-1  (학생 수) } 
    for j in range(1,lenth):
        if(score[j]>average):
            count+=1                                     #해당 리스트의 평균을 구하고 평균값을 넘는 학생 수->count변수에 넣어줌
    ratio=(count)/(lenth-1)*100                           #평균넘는 학생들의 비율
    ratio=format(ratio,".3f")                                #소숫점 세자리로 포맷
    print("{0}%".format(ratio))                            #출력
        
