def check_used_times(ch_list):
    lenth1=len(ch_list)
    set_ch_list=set(ch_list)
    lenth2=len(set_ch_list)
    if lenth1==lenth2:
        return 0
    else :
        return 1
        
n=int(input())
count=0
flag=0
for i in range(0,n):
    flag=0
    used_character=[]     #['c','a','z','a']
    s=input()                #ccazza
    s=list(s)               
    if len(s) == 1:
        count+=1
        continue
    tmp=s[0]
    used_character.append(s[0])
    for j in range(1,len(s)):
        if s[j]!=tmp:           
            used_character.append(s[j])
            tmp=s[j]             
    flag=check_used_times(used_character)
    if flag==0:
        count+=1
    else:
        continue
print(count)
