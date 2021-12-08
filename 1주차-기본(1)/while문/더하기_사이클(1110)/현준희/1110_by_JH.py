count=0
n=int(input())
k=n
flag=1
while flag==1 :
    one=k%10
    ten=int(k/10)
    newone=(ten+one)%10
    k=one*10+newone
    count+=1
    if k==n :
        break;
print(count)
