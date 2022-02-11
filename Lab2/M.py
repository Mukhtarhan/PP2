lit=[]
a=int()
def dd(arr):
    arr.sort()
    return arr 
while a==0:
    st=[]
    s=(input())
    st=s.split(" ")
    if st[0]!= '0':
        b=st[2]+" "+st[1]+" "+st[0]
        lit.append(b)
        
    if '0' in st:
        break
dd(lit)
for i in lit:
    t=[]
    t=i.split(" ")
    print(t[2]+" "+t[1]+" "+t[0])

