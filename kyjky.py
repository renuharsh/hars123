int(input())
m=list(map(int,input().split()))
l=[]
for i in m:
    if m.count(i)>1:
        l.append(i)
l=list(set(sorted(l)))
if len(l)>0:
    for i in range(len(l)-1):
        print(l[i],end=' ')
    print(l[len(l)-1],end='')
else:
    print("unique")    
