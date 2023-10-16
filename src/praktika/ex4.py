def normalize(array: list):
    return [i if i != 3 else 4 for i in array if i != 2]

array1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4] 
array2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4] 
array3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print(f"first: {array1}\nformatted: {normalize(array1)}\n")
print(f"second: {array2}\nformatted: {normalize(array2)}\n")
print(f"third: {array3}\nformatted: {normalize(array3)}\n")