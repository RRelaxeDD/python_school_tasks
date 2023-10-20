def tuple_sort(tpl):
    for elem in tpl:
        if not isinstance(elem, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == "__main__":
    print(tuple_sort((5, 5, 3, 1, 9)))
    print(tuple_sort((5, 5, 2.1, "1", 9)))
