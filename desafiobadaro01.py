import math

x = float(input('Digite o tamanho do primeiro lado: '))
y = float(input('Digite o tamanho do segundo lado: '))
z = float(input('Digite o tamanho do terceiro lado: '))
if x < y + z and y < x + z and z < x + y:
    s = (x + y + z) / 2
    h = (2/x) * math.sqrt(s*(s-x)*(s-y)*(s-z))
    print(f'A altura para base {x} é: {h:.2f}')
    print(f'A área é: {x * h / 2:.2f}')
    if x == y == z:
        print('O Triângulo é equilátero')
    elif x != y and y != z and x != z and (x**2 == y**2+z**2 or y**2 == x**2+z**2 or z**2 == x**2+y**2):
            print('O triângulo é escaleno e um triângulo retângulo')
    elif (x == y and y != z) or (x != y and y == z) or (x == z and z != y):
                 print('O triângulo é isósceles')
    else: print('O triângulo é escaleno, mas não é um triângulo retângulo')
else: print('Não é possível formar um triângulo com as medidas especificadas.')
