import sys
from collections import Counter     #most_common() 함수 쓰기 
def alphabet_index(s):
    k=Counter(s).most_common(2)
    if k[0][1]==k[1][1] :
        print('?')
    else:
        print(k[0][0])
s=input()
if len(s)==1:
    if ord(s) >=97 and ord(s)<=122:
        s=chr(ord(s)-32)
    print(s)
    sys.exit()
s=list(s)
lenth=len(s)
for i in range(0,lenth):
    if ord(s[i]) >= 97 and ord(s[i]) <=122 :
        K=ord(s[i])
        s[i]=chr(K-32)
alphabet_index(s)
