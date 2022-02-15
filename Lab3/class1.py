class ddd:
    def __init__(s,string):
        s.string=string
    
    def get_string():
        s=input()
        return s
    def printstring(s):
        t=s.string
        s.string=t.upper()
        print(s.string)
st=ddd.get_string()
p1=ddd(st)
p1.printstring()
