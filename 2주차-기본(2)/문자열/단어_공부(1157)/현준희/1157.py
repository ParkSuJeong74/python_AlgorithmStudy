import sys                              
from collections import Counter                   # most_common() 함수 쓰기(최빈값 찾기) ex) ['M','I','S','S','I','S','S','I','P','I']   
def alphabet_index(s):                            # 전달받은 원소가 대문자로만 이루어진 리스트에서 가장많이 중복된 원소를 찾고 그것을 출력하는 함수 
    k=Counter(s).most_common(2)                   # 최빈값 두개를 찾는다(가장많이 나온 알파벳이 여러개 존재하는 경우도 따져야함)   K==[('I',4) , ('S',4)] I가 4번 S가 4번 이라는 뜻
    if k[0][1]==k[1][1] :                         # k[0][1]==4(==I가 나온 횟수) k[1][1]==4(==S가 나온 횟수)   : 가장 많이 들어간 알파벳이 여러개임
        print('?')                                # ? 출력 
    else:                                         # ex) ['A','A','A','B','B,'C,'C'] -> k==[('A',3) , ('B',2)] , k[0][1]==3 , k[1][1]==2   
        print(k[0][0])                            # k[0][0[]=='A'
s=input()                                         # 단어 입력      ex)Mississipi
if len(s)==1:                                     # 알파벳 하나로 이루어졌을 때
    if ord(s) >=97 and ord(s)<=122:               # 소문자일 때
        s=chr(ord(s)-32)                          # 대문자로 바꿈
    print(s)                                      # 출력
    sys.exit()                                    # 종료
s=list(s)                                         # 문자열 리스트화
lenth=len(s)                                      # 리스트 길이  
for i in range(0,lenth):                          # 리스트 인덱스 0부터 끝까지 모든 원소들을 소문자가 있으면 대문자로 교체하는 반복문
    if ord(s[i]) >= 97 and ord(s[i]) <=122 :      # 소문자일 경우
        K=ord(s[i])                               # 
        s[i]=chr(K-32)                            # 대문자로 바꾸기
alphabet_index(s)                                 # alphabet_index호출, 모두 대문자로 통일한 리스트 전달    ex) ['M', 'I', 'S', 'S', 'I', 'S', 'S', 'I', 'P', 'I']
