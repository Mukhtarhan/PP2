class Point:
    
    def __init__(coor,x,y,x2,y2):
        coor.x=x
        coor.y=y
        coor.y2=y2
        coor.x2=x2
    def show(coor):
        print(x,y)
    def move(coor):
        coor.x+=1
        coor.y+=1
    def dist(coor):
        import math 
        dis=pow(x2-x,2)+pow(y2-y,2)
        dis=math.sqrt(dis)
