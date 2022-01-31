s=input()
t=str()
s=s.split()
for i in range(len(s)):
    if len(s[i])>=3:
        t=t+s[i]+" "
print(t)
