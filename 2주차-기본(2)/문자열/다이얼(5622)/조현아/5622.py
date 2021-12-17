A = ["ABC","DEF","GHI","JKL", "MNO", "PQRS", "TUV", "WXYZ"]
B = list(input())
time = 0
for i in B :
    for o in A :
        if i in o :
            time += A.index(o)+3
print(time)
