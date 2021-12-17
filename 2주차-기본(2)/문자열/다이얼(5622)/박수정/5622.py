alpa = list(map(chr, range(65, 91)))
dial = []
count = 0
s = ""
for i in alpa:
    count += 1
    s += i
    if i != "R" and i != "Y":
        if count % 3 == 0 or i == "S" or i == "Z":
            dial.append(s)
            s = ""
            count = 0

time = 0
string = list(input())
for i in string:
    for j in dial:
        if i in j:
            time += dial.index(j)+3
print(time)
