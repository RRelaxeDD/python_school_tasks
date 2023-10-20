# посчитать сумму четных чисел в массиве
def sum_of_enen_numbers(obj):
    return sum([i for i in obj if i % 2 == 0])

print(sum_of_enen_numbers([17, 17, 5, 15, 15, 3, 14, 3, 9, 2, 1, 1, 2, 14, 8, 14, 18, 14, 2, 1]))