t={}
cnt=int()
a=int(input())
for i in range(a):
    s=input()
    s=s.split(" ")
    if s[1] in t:
        t[s[1]]+=1
        cnt+=1
    else :
        t[s[1]]=1
        cnt+=1
b=int(input())
for i in range(b):
    b,c,d=input().split(maxsplit=2)
    if c in t and t[c]<=int(d):
        cnt-=t[c]
        t.pop(c)
        
    if c in t and t[c]>int(d):
        cnt=cnt-int(d)
        t[c]=t[c]-int(d)
        
print("Demons left:",cnt)        
         
        
