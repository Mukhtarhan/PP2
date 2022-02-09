s=input()
v=[]
t=[",",".","!","?"]
st=s.split(' ')


st.sort()
for i in range(len(st)):
    p=st[i]
    if t[0] in p:
        st[i]=p[0:len(p)-1]
    if t[1] in p:
        st[i]=p[0:len(p)-1]
    if t[2] in p:
        st[i]=p[0:len(p)-1]
    if t[3] in p:
        st[i]=p[0:len(p)-1]
    else :
        continue

for i in range(len(st)):
    if st[i] in v:
        continue
    else :
        v.append(st[i])
print(len(v))    
for i in range(len(v)):
    print(v[i])
