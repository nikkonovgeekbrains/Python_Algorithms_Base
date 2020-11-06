print("Введите координаты первой точки")
x1 = int(input("x= "))
y1 = int(input("y= "))
print("Введите координаты второй точки")
x2 = int(input("x= "))
y2 = int(input("y= "))

k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1

print(f'Данные точки принадлежат кривой y={k}*x+{b}')
