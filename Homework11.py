from math import atan

x = int(input("Введите значение Х"))
y = int(input("Введите значение Y"))
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def to_polar (self):
        self.r = ((self.x**2)+(self.y**2))**0.5
        self.f = atan(self.x/self.y)
        return (self.r,self.f)



point_1 = Point(x,y)
point_1.to_polar()
print(point_1.x,point_1.y)
print(point_1.r,point_1.f)


