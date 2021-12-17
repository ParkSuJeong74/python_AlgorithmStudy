def task_time(ch):                     # 알파벳에 따른 리턴 값(==소모시간)
    return {
        'A':1,'B':1,'C':1,
        'D':2,'E':2,'F':2,
        'G':3,'H':3,'I':3,
        'J':4,'K':4,'L':4,
        'M':5,'N':5,'O':5,
        'P':6,'Q':6,'R':6,'S':6,
        'T':7,'U':7,'V':7,
        'W':8,'X':8,'Y':8,'Z':8
        }[ch]
count=0                              #최종 걸리는 시간 저장할 카운트 변수
s=input()                            #문자열 입력
lenth=len(s)                         #문자열 길이
s=list(s)                            #리스트화
for i in range(0,lenth):             #리스트 원소(알파벳) 하나씩 걸리는 시간 계산
    count+=2
    count+=task_time(s[i])       
print(count)
