def replace(inpu_list):
    # memory = inpu_list[0]
    # inpu_list[0] = inpu_list[-1]
    # inpu_list[-1] = memory
    inpu_list[0], inpu_list[-1] = inpu_list[-1], inpu_list[0]
    return inpu_list

print(replace([1, 2, 3, 4, 5]))