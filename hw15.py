from math import sqrt
class Figure:
    def __init__(self):
        pass

    def Square(self):
        pass

    def Perimeter(self):
        pass

class Triangl(Figure):

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def Square(self):
        p = (self.a+self.b+self.c)/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def Perimeter(self):
        return self.a + self.b + self.c

class Circle(Figure):

    def __init__(self,r):
        self.r = r

    def Perimeter(self):
        return 2 * (3.14) * self.r

    def Square(self):
        return (3.14) * (self.r **2)

class Square(Figure):

    def __init__(self,d):
        self.d = d

    def Perimeter(self):
        return 4 * self.d

    def Square(self):
        return self.d ** 2

a = int(input("Введите сторону триугольника a "))
b = int(input("Введите сторону триугольника b "))
c = int(input("Введите сторону триугольника c "))
r = int(input("Введите радиус круга r "))
d = int(input("Введите сторону квадрата d "))

trinangle = Triangl(a,b,c)
square = Square(d)
circle = Circle(r)

print("Периметр триугольника: ", trinangle.Perimeter(),"Площадь триугольника: ", trinangle.Square())
print("Перметр круга: ", circle.Perimeter(), "Площадь круга: ", circle.Square())
print('Периметр квадрата: ',square.Perimeter(),'Площадь квадрата: ', square.Square())