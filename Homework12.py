x1 = int(input("Введите значение Х1"))
y1 = int(input("Введите значение Y1"))
x2 = int(input("Введите значение Х2"))
y2 = int(input("Введите значение Y2"))
b = int(input("Введите значение B"))
class Vector:
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

    def sum (self):
        self.sum_ab=(self.x1+self.x2), (self.y1+self.y2)

    def minus(self):
        self.minus_ab=(self.x1-self.x2), (self.y1-self.y2)

    def mult(self):
        self.mult_ab=(self.x1*b),(self.y1*b)
        self.mult_ab1=(self.x2*b),(self.y2*b)

vector=Vector(x1,x2,y1,y2)
vector.sum()
vector.minus()
vector.mult()
print(vector.sum_ab,vector.minus_ab,vector.mult_ab, vector.mult_ab1)

