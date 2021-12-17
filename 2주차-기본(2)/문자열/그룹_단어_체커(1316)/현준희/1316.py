def check_used_times(ch_list):       # 그룹단어인지 확인하는 함수, 매개변수로는 리스트를 받음. ex)  ['c', 'a', 'z', 'a']
    lenth1=len(ch_list)              # lenth1=전달받은 리스트의 길이.  ['c', 'a', 'z', 'a'] -> lenth1=4
    set_ch_list=set(ch_list)         # 전달받은 리스트를 집합으로 변경.->  {'c', 'a', 'z'}  -> 중복되는 원소가 없어짐. 
    lenth2=len(set_ch_list)          # lenth2=기존 리스트에서 중복을 없앤 집합의 길이 {'c', 'a', 'z'}  -> lenth2=3
    if lenth1==lenth2:               # 만약 전달받은 리스트가 중복원소가 없는 리스트라면 lenth2==lenth1 임 
        return 0                     # 리턴값 0 : 중복이 없으니 그룹단어가 맞다.
    else :                           # 중복원소가 존재하는 리스트
        return 1                     # 리턴갓 1: 중복이 있으니 그룹단어가 아니다.
        
n=int(input())                                 # 첫째 줄에 입력받을 단어의 개수
count=0                                        # 그룹 단어 개수를 저장할 카운트변수                                        
for i in range(0,n):                           # 단어의 개수 n 만큼 반복함
    flag=0                                     # 그룹단어 판별 함수로 전달받은 리턴값에 따라 변하는 플래그변수
    used_character=[]                          # 입력받은 단어를 읽다가 같은 알파벳의 연속이 끊기고 다른 알파벳이 나오면 해당 알파벳을 원소로 저장할 리스트 
    s=input()                                  # 입력받을 단어   ex)ccazza
    s=list(s)                                  # 입력받은 단어(문자열) 을 리스트화
    if len(s) == 1:                            # 단어의 길이가 1일때(==알파벳 하나만 입력 됐을 경우)
        count+=1                               # 그룹 단어이니 카운트+1 하고 continue 하고 다시 단어입력하는 단계로 넘어감.
        continue                               # "
    tmp=s[0]                                   # 임시변수에 첫 알파벳넣어줌 ( 다음에 나올 알파벳과 비교하기 위함 )
    used_character.append(s[0])                # 처음 등장한 알파벳을 리스트에 추가
    for j in range(1,len(s)):                  # 리스트 인덱스 1부터 끝까지
        if s[j]!=tmp:                          # 등장한 알파벳 값과 임시변수값이 다를 때(알파벳의 연속이 끊길 때)
            used_character.append(s[j])        # 리스트에 추가
            tmp=s[j]                           # 임시변수에 리스트에 추가한 알파벳을 넣어줌
    flag=check_used_times(used_character)      # 리스트에 연속이 끊겼던 모든 알파벳들을 넣어주고 그룹단어인지 확인
    if flag==0:                                # 그룹단어일 때
        count+=1                               #
    else:                                      # 아닐 
        continue                            
print(count)   
