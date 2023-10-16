import geron

side1 = float(input("Введите длину стороны 1: "))
side2 = float(input("Введите длину стороны 2: "))
side3 = float(input("Введите длину стороны 3: "))

result = geron.s_triangle(
    side1,
    side2,
    side3
)
print(f"площадь треугольника: {result}")