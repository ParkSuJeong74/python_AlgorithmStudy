num_a = set(range(1,10001))
num_b = set()

for i in range(1,10001):
    for o in str(i):
        i += int(o)
    num_b.add(i)
    
self_num = sorted(num_a - num_b)
for i in self_num:
    print(i)
