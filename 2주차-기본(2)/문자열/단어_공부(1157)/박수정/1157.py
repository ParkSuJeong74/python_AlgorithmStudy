import sys

s = list(sys.stdin.readline().upper())
s.pop()
arr = list(set(s))  # 중복 없음
cnt = [s.count(i) for i in arr]

if cnt.count(max(cnt)) == 1:
    print(arr[cnt.index(max(cnt))])
else:
    print("?")
