j=int()
a=int()
st=[]
while j==0:
    
    st.append(int(input()))
    if 0 in st:
        break

for i in range(int(len(st)/2)):
    if len(st)%2==0 and i==(len(st)/2)-1:
        print(st[i],end=" ")
        continue
    print((st[i])+st[len(st)-2-i],end=" ")
    if i>=len(st)/2:
        break
