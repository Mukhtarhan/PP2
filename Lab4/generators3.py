class Numbers:
    def __init__(self,value,last):
        self.value=value
        self.last=last
    def __iter__(self):
        return self
    def __next__(self):
        if self.value<=self.last:
            x=self.value
            self.value+=1
            if x%3==0 and x%4==0 and x!=0:
                return x
        else:
            raise StopIteration
n=int(input())
mynumbers = Numbers(0,n)
myiter = mynumbers
for i in myiter:
    if type(i)==int:
        print(i)
            
