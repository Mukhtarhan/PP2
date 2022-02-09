a=int(input())
for i in range(a):
    for j in range(a):
        if a%2==0:
            if j<=i:
                print('#',end='')
            else :
                 print('.',end='')
        else:
             if j+i>=a-1:
                 print('#',end="")
             else :
                 print('.',end='')
            
    print('\n',end='')
