a=int(input())
t={}
x=[]
mx=0
for i in range(a):
    b,c=input().split(maxsplit=1)
    if b in t:
        t[b]+=int(c)
        if mx<t[b]:
            mx=t[b]
    else:
        t[b]=int(c)
        x.append(b)
        if mx<t[b]:
            mx=t[b]

x.sort()
for i in x:
    if t[i]==mx:
        print(i,"is lucky!")
    else:    
        print(i,"has to receive",mx-t[i],"tenge")
    
