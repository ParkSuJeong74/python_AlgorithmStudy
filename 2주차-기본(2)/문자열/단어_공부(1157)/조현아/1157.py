A = input().upper()
B = list(set(A))
C = []

for i in B:
    C.append(A.count(i))    
if C.count(max(C)) > 1 :
    print("?")
else : 
    print(B[C.index(max(C))])
