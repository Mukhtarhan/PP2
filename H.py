s=input()
t=input()
cnt=0
ans=int()
ans2=int()    
for i in range(len(s)):
    if s[i]==t:
        ans=i
        break
for i in range(len(s)):
    if s[len(s)-1-i]==t:
        ans2=len(s)-1-i
        break
if ans==ans2:
    print(ans)
else:
    print(ans,ans2)
