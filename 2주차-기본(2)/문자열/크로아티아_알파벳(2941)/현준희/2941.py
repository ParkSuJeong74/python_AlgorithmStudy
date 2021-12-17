c_list=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
count=0
new_s=[]
for i in range (0,8):
    s=s.replace(c_list[i],'1')
count=len(s)
print(count)
