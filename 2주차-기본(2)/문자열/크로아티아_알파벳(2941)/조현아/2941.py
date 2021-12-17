A = 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='
B = input()
for i in A:
    B = B.replace(i,'^')
print(len(B))
