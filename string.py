lens = len(s)
lent = len(t)
count = 0
for i in range(abs(lens - lent + 1)):
    count += 1
    if t == s[i:(i + lent)]:
        return print("В строке s есть подстрока t ")
    elif count < (lens - lent + 1):
        continue
    else:
        return print("В строке s нет подстрока t")

def is_number(s):
    if isinstance(s, str):
        print ('Строка не являэться числом')
    else:
        print ('Строка являэться числом')

def is_case_insensitive_equal(s, t):
    if s.upper().lower() == t.upper().lower():
        print('Одинаковые строки')
    else:
        print ('Неодинаковые строки')

'''
- функция проверяет есть ли в строке s подстрока t. Мы такую задачу решали в предыдущих заданиях.
 - проверяет что строка является числом. Например, строка "1234" является числом, а строка "abc12" не является.
 - проверяет что строки одинаковы, даже если отличаются регистром букв. Например, "AAbbAA"
одинаковая со строкой "aaBBaA"
'''