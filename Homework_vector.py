x1 = int(input("Введите значение Х1"))
y1 = int(input("Введите значение Y1"))
x2 = int(input("Введите значение Х2"))
y2 = int(input("Введите значение Y2"))
K = int(input("Введите значение K"))


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,B):
        print('__add__ method is called')
        return (self.x + B.x), (self.y + B.y)


    def __sub__(self,B):
        print('__sub__ method is called')
        return (self.x - B.x), (self.y - B.y)

    def __mul__(self,K):
        print('__mul__ method is called')
        return (self.x * K), (self.y * K)

A = Vector(x1, y1)
B = Vector(x2, y2)

print('A + B =', A + B)
print('A - B =', A - B)
print('A *', K, '= ', A * K)
print('B *', K, '= ', B * K)