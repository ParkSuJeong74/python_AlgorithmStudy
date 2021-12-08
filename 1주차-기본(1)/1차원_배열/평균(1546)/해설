n=int(input())          
score=list(map(int,input().split()))           //점수담을 리스트 
m=max(score)                                    //리스트 내에서의 최댓값
for i in range(n):
    score[i]=score[i]/m*100                       //모든 점수들을 변경해줌
hab=0                        //새로운 평균 짜기 위한 변수
for i in range(n):
    hab+=score[i]                  //수정된 모든 점수 합
new_average=hab/n                //새로운 평균
print(new_average)               //출력
