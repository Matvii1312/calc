import math
print('''\nМеню:\n\t1. сложение\n\t2. вычитание\n\t3. умножение\n\t4. деление\n\t5.возведение в степень\n\t6.квадратный корень\n\t7.кубический корень\n\t8. Выход
''')
while True:
    responce = input('Выберите действие:')
    a = int(input('a: '))
    b = int(input('b: '))
    if responce == '1':
        def add(a, b):
            return a + b
        print(add(a, b))


    elif responce == '2':
        def sub(a, b):
            return (a -b)
        print(sub(a, b))


    elif responce == '3':
        def mult(a, b):
            return (a * b)
        print(mult(a, b))