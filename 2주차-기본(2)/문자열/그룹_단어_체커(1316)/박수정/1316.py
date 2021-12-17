import sys

# 그룹단어 판별 함수
def checker(string):
    # 한 문자씩
    for i in range(len(string)-1):
        # 두 연속하는 문자가 같지 않고
        if string[i] != string[i+1]:
            # 이전 문자에 이미 존재함
            if string[i+1] in string[:i]:
                return False
    return True # 해당하지 않으면 그룹단어

n = int(sys.stdin.readline())

idx= 0
for i in range(n):
    string = str(sys.stdin.readline())
    # 그룹단어면 갯수 카운트
    if checker(string) == True :
        idx +=1
print(idx)
