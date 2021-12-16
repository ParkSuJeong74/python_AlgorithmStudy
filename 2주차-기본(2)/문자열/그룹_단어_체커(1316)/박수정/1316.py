import sys

def checker(string):
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] in string[:i]:
                return False
    return True

n = int(sys.stdin.readline())

idx= 0
for i in range(n):
    string = str(sys.stdin.readline())
    if checker(string) == True :
        idx +=1
print(idx)
