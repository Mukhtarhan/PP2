a=int(input())
b=input()
ok=False
res=str()
cnt=0
if b=='k':
    dig=int(input())
    ans=a/1024
    print(round(ans,dig))
    
else:
    ans=a*1024
    print(ans)    
