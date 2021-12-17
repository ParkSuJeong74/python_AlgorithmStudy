def d_n(a):
    k1=(a%10)
    k2=(a%100)//10
    k3=(a%1000)//100
    k4=a//1000
    k=a+k1+k2+k3+k4
    return k
numbers=[0 for i in range(100001)]        #리스트 10000번째 인덱스까지 0으로초기화
for i in range(10000):
    if d_n(i) <= 10000:
        index=d_n(i)
    numbers[index]=1
for i in range(10000):
    if numbers[i]==0:
        print(i)
