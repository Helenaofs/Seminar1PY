# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите x, число 1 или 0: '))
y = int(input('Введите y, число 1 или 0: '))
z = int(input('Введите z, число 1 или 0: '))

disjunction = x + y + z
conjunction = x * y * z

if disjunction > 0:
    disjunction = 1
elif disjunction < 1:
    disjunction = 1
    
if conjunction > 0:
    conjunction = 0
elif conjunction < 1:
    conjunction = 1

if conjunction == disjunction:
    print('Утверждение истинно')
elif conjunction != disjunction:
    print('Утверждение ложно')
