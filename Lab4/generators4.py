def squares(a,b):
    while a<b:
        num=a*a
        yield num
        a+=1
res = squares(1, 5)
for i in range(1, 5):
    print(next(res))

