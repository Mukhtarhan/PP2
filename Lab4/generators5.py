def gen(n):
    num=n
    while num>=0:
        yield num
        num-=1
res = gen(10)
i=10;
while i>=0:
    print(next(res))
    i-=1
