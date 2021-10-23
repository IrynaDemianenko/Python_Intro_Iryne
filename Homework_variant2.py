x1 = int(input("Введите значение Х1"))
y1 = int(input("Введите значение Y1"))
x2 = int(input("Введите значение Х2"))
y2 = int(input("Введите значение Y2"))
b = int(input("Введите значение B"))
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def sum (self,B):
        sum_ab=(self.x+B.x),(self.y+B.y)
        return sum_ab

    def minus(self,B):
        minus_ab=(self.x-B.x),(self.y-B.y)
        return minus_ab

    def mult(self,b):
        mult_ab=(self.x*b),(self.y*b)
        return mult_ab

A=Vector(x1,y1)
B=Vector(x2,y2)

print('A + B =',A.sum(B))
print('A - B =',A.minus(B))
print('A *',b,'= ',A.mult(b))
print('B *',b,'= ', B.mult(b))



