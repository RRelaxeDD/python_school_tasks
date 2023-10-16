def s_triangle(x, y, z):
    '''
    x, y, z - стороны треугольника

    возвращает площадь треугольника по формуле Герона
    '''
    p = (x + y + z) / 2
    s = (p * (p - x) * (p - y) * (p - z)) ** 0.5
    return s


one = [12, 25, 3, 48, 71] 
two = [5, 18, 40, 62, 98] 
three = [4, 21, 37, 56, 84]

first_min = [min(one), min(two), min(three)]
second_max = [max(one), max(two), max(three)]

s_first = s_triangle(first_min[0], first_min[1], first_min[2])
s_second = s_triangle(second_max[0], second_max[1], second_max[2])

print(f"стороны первого треугольника: {first_min}\nплощадь: {s_first}")
print(f"стороны второго треугольника: {second_max}\nплощадь: {s_second}")