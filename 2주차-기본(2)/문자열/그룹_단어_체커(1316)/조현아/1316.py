N=int(input())
for i in range(N):
    a=input()
    if list(a)!=sorted(a,key=a.find):
        N-=1
print(N)
