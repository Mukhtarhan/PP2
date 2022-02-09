import math
r={}
t=[]
a, b=list(map(int,input().split()))
n=int(input())
for i in range(n):
    c,d=list(map(int,input().split()))
    val=(c-a)**2+(d-b)**2
    val=math.sqrt(val)
    t.append(val)
    r[val]=str(c)+" "+str(d)
t.sort()
for i in range(len(t)):
    print(r[t[i]])
