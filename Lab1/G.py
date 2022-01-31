s=str(input())
s=s[::-1]
sum=0
for i in range(len(s)):
    sum=sum+(ord(s[i])-48)*pow(2,i)
print (sum)    
