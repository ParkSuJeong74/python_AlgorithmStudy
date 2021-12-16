def d(n):
    # 생성자를 입력받으면 결과를 리턴하는 함수
    not_self_number = list(map(int, str(n)))
    result = n
    result += sum(not_self_number)
    return result # n을 생성자를 가지는 수

arr = list(range(1, 10001))
arr_del = set([])

for i in range(10000):
    arr_del.add(d(i))
arr_del_list = list(arr_del)
result = list(set(arr).difference(arr_del_list))
result.sort()
for i in result:
    print(i)
