a=int(input())
ind=int()
t="@"
for i in range(a):
    s=input()
    for j in range(len(s)):
        if s[j]==t:
            ind=j
    if '@gmail.com' in s:
        s=s[:ind]
        print(s)
