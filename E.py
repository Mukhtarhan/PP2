a,f=map(int,input().split())

true=int()
import math
if a<=500:
    b=round(math.sqrt(a))
    for i in range(2,b):
        if a%i != 0:
            true=1
            
        else :
            true=0
            break
else:
    true=0
            
if true==1:
    if f%2==0:
        print("Good job!")
    else:    
        print("Try next time!")
else :
    print("Try next time!")
