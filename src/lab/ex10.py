global result

def rectangle():
    a = float(input("width: "))
    b = float(input("height: "))
    global result
    result = a + b

def triangle():
    a = float(input("base: "))
    h = float(input("height: "))
    global result
    result = 0.5 * a * h

figure = input("1 - прямоугольник\n2 - треугольник\ninput: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")
