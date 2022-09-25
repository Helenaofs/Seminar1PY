# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

print('Введите координаты точки А:')
x_pointA = float(input('x: '))
y_pointA = float(input('y: '))
print('Введите координаты точки В:')
x_pointB = float(input('x: '))
y_pointB = float(input('y: '))

distance = (((x_pointB - x_pointA) ** 2) + ((y_pointB - y_pointA) ** 2)) ** 0.5
print(round((distance), 2))

