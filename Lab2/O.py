s=input()
ind=int()
res=int()
ans=int()
res2=int()
ind2=s.index('+')
t=["ZER","ONE","TWO","THR","FOU","FIV","SIX","SEV","EIG","NIN","ZER"]
for i in range(len(s)-2):
    if (s[i]+s[i+1]+s[i+2]) in t and i<ind2:
        ind=t.index(s[i]+s[i+1]+s[i+2])
        res=res*10+ind
    if (s[i]+s[i+1]+s[i+2]) in t  and i>ind2:
        ind=t.index(s[i]+s[i+1]+s[i+2])
        res2=res2*10+ind
ans=res+res2
s=str(ans)
v=str()
for i in range(len(s)):
    v=v+t[ord(s[i])-48]
print(v)          
