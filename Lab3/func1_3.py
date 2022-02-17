def solve(numheads,numlegs):
    for i in range(1,36):
        if (i*2)+(35-i)*4==94:
            return str(i)+" "+str(35-i)
print(solve(35,94))
    
