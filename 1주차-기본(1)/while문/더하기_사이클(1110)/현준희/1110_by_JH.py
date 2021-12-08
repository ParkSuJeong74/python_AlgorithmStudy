count=0
n=int(input())          # 정수 N 입력   26을 입력받았다고 가정
k=n                   #임의의 변수 k에 N값을 저장    k->26 
while 1 :      
    one=k%10        #     일의자리 분리 26->6  :one=6
    ten=int(k/10)             #십의자리 분리 26->2 :ten=2
    newone=(ten+one)%10           # 새로운 일의자리 구하기 26->2+6 ->8      2+6(ten+one)%10=8
    k=one*10+newone         # 6*10 + 8 -> 68                
    count+=1                #사이클 길이 누적
    if k==n :              #while반복문 안에서 사이클을 계속 돌다 원래 수 N이 되면 사이클 종료
        break;
print(count)             #누적된 사이클 길이 출력
