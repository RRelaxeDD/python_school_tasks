def del_elem_from_tuple(tpl, elem):    
    if elem not in tpl: return tpl

    tpl = list(tpl)
    tpl.remove(elem)
    
    return tuple(tpl)

print(del_elem_from_tuple((1, 2, 3), 1))
print(del_elem_from_tuple((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(del_elem_from_tuple((2, 4, 6, 6, 4, 2), 9))