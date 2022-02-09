ar=list(map(int,input().split()))
n=len(ar)-1
def dd(i,arr,n):
    if i>=n:
        return 1
    if arr[i]==0:
        return 0
    if i==0 and arr[i]!=1:
        return dd(arr[i]-1,arr,n)
    else:
        return dd(arr[i]+i,arr,n)

print(dd(0,ar,n)) 
    
    
