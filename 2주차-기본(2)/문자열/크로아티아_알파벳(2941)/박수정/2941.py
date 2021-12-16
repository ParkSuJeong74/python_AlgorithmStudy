string = str(input())
croa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0

for i in croa:
    if i in string: # string에 크로아티아 문자 존재
        count+=string.count(i)
        string = string.replace(i, "-")
string = string.replace("-", "")
print(count+len(string))
