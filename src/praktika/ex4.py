def cut_tuple_from_elem(tpl, id):
    if id not in tpl:
        return ()
    return tpl[tpl.index(id):]

print(cut_tuple_from_elem((1, 2, 3), 8))
print(cut_tuple_from_elem((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(cut_tuple_from_elem((1, 2, 8, 5, 1, 2, 9), 8))