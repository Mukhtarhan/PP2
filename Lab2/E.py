a=list(map(int, input().split()))
if len(a)==1:
    c=int(input())
    a.append(c)
b=[]
for i in range(a[0]):
    res=a[1]+2*i
    b.append(res)
ans=b[0]
for i in range(1,len(b)):
    ans=ans^b[i]
print(ans)    
