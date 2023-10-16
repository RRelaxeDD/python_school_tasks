def normilize(array: list):
    new_array = []
    array_set = list(set(array))
    for i in array_set:
        amount = array.count(i)
        new_array.append(i)
        if amount > 1:
            for j in range(2, amount+1):
                new_array.append(str(i) * j)
    return new_array

list_1 = [1, 1, 3, 3, 1] 
list_2 = [5, 5, 5, 5, 5, 5, 5] 
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(f"first: {list_1}\nnew: {normilize(list_1)}\n")
print(f"second: {list_2}\nnew: {normilize(list_2)}\n")
print(f"third: {list_3}\nnew: {normilize(list_3)}\n")