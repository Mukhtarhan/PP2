class Numbers:
    def __init__(self,last,value):
        self.value=value
        self.last=last
    def __iter__(self):
        return self
    def __next__(self):
        
        if self.value<self.last:
            x = self.value
            self.value += 1
            return pow(x,2)
        else:
            raise StopIteration
n=int(input())    
myNumbers = Numbers(n,1)
myiter = iter(myNumbers)
for x in myiter:
    print(x)
