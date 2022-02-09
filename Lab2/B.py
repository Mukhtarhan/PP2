a=int(input())
b=[]
b=list(map(int, input().split()))
b.sort()
res=b[a-1]*b[a-2]    

print(res)    
