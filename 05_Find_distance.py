# Программа принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве: (3,6); B (2,1) -> 5,09.

x1 = float(input('Введите х для точки A: '))
y1 = float(input('Введите y для точки A: '))
x2 = float(input('Введите х для точки B: '))
y2 = float(input('Введите y для точки B: '))

distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
print(round(distance,3))