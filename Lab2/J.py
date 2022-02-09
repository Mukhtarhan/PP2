a=int(input())
n=[0,0,0]
t=[]
for i in range(a):
    s=input()
    for j in range(len(s)):
        if ord(s[j])>=65 and ord(s[j])<=90:
            n[0]=1
        if ord(s[j])>=48 and ord(s[j])<=57:
            n[1]=1
        if ord(s[j])>=97 and ord(s[j])<=122:
            n[2]=1
    if n[0]+n[1]+n[2]==3 and s not in t:
        t.append(s)
    n=[0,0,0]
t.sort()
print(len(t))
for i in range(len(t)):
    print(t[i])
