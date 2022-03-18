def count_upper(s):
    cnt=0
    for i in s:
        
        if  ord(i)>=65 and ord(i)<=90:
            cnt+=1
    return cnt
print(count_upper("SHKslsk"))
