a=int(input())
st=[]
for i in range(a):
    s=input()
    s=s.split(" ")
    if s[0]=="1":
        st.append(s[1])
    else:
        print(st[0],end=" ")
        st.remove(st[0])
