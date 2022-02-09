a=int(input())
for i in range(a):
    
    for j in range(a):
        if i==0 or j==0:
            print(j+i,end=' ')
            continue
        if j==i and i!=0:
            print(i*j,end=" ")
            continue
        else:
            print(0, end=" ")
            continue
    print('\n',end='')
