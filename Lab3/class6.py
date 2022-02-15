def filter(n):
    for i in range(2,int(n/2)):
        if n%i==0:
            return "Not prime"
        else:
            continue
    return "Prime"        
a=int(input())
print(filter(a))
