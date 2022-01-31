a=input()
sum=0
for i in a:
    sum=ord(i)+sum
    
if(sum>300):
    print('It is tasty!')
else:
    print('Oh, no!')
