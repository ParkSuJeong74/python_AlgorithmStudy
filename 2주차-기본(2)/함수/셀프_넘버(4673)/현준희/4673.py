def d_n(a):                       #함수 d(n)
    k1=(a%10)
    k2=(a%100)//10
    k3=(a%1000)//100
    k4=a//1000
    k=a+k1+k2+k3+k4
    return k
numbers=[0 for i in range(100001)]        #리스트 10000번째 인덱스까지 0으로초기화  numbers[0]=0,numbers[1]=0,........,numbers[10000]=0    
for i in range(1,10001):                    #i=1부터 10000까지 
    if d_n(i) <= 10000:                   # 10000보다 같거나 작은 모든 d(n)을 구함.    
        index=d_n(i)                      # i가 1부터 들어갔을 때 d(i)값 ->index
    numbers[index]=1                      #numbers[index]에 1을 넣어줌 : d(i)(==index)값이 존재한다는 것 ( numbers[1],numbers[3],....numbers[9993]  )은 해당이 안되니 셀프넘버라는 뜻
for i in range(1,10000):                # 
    if numbers[i]==0:                   # numbers[1] 부터 numbers[10000]까지 값이 1이 아닌(==셀프넘버일때)
        print(i)                  
