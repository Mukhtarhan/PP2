class MyNumbers():
    def __init__(self,current,last):
        self.current=current
        self.last=last
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.last:
            x=self.current
            self.current += 2
            return x
        else :
            raise StopIteration
n=int(input())
Evens = MyNumbers(2,n)
myiter = iter(Evens)
for i in myiter:
    print(i,end=", ")
