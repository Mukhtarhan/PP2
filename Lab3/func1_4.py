def filter_prime(arr,i,length):
    if i>length:
        return ""
    for j in range(2,int(arr[i]/2)+1):
            if arr[i]%j==0:
                return filter_prime(arr,i+1,length)
    else:
        print(arr[i],end=" ")
        return filter_prime(arr,i+1,length)
        
ar=list(map(int,input().split()))
print(filter_prime(ar,0,len(ar)-1))
