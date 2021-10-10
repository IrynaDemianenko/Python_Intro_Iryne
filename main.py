import calc

string = input('Введите задачу: ')
a = int(string[0])
b = int(string[2])
if string[1] =='+': calc.sum(a,b)
elif string[1] == '*': calc.mult(a,b)
elif string[1] == '/':calc.div(a,b)
elif string[1] == '-': calc.minus(a,b)

'''Задача 1.
Нужно будет реализовать калькулятор для простых математических выражений.
Выражение представляет из себя строчку вида "number1 operation number2", где
number1, number2 числа, а operation - это  что одно из "+", "-", "*", "/"
Примеры выражений: "1 + 2", "3 - 2", "4 * 2", "15 / 3"
Результатом решения будут два модуля: calc.py и main.py
calc.py реализуйте логику обработки математических выражений, а в main.py ввод/вывод данных и вызов методов
нужных методов из calc.py
'''