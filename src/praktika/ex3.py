def get_most_frequent_numbers_from_str(user_input):

    numbers = tuple((int(i) for i in user_input))

    vales_dict: dict[str, int] = {}
    for i in numbers:
        if i in vales_dict:
            vales_dict[i] += 1
        else:
            vales_dict[i] = 1

    result_dict = {}
    for i in sorted(vales_dict, key=lambda x: vales_dict[x])[-3:]:
        result_dict[i] = vales_dict[i] 
    return result_dict


print(get_most_frequent_numbers_from_str("01897362673264426992"))
print(get_most_frequent_numbers_from_str("36488233557900891306"))
print(get_most_frequent_numbers_from_str("56083612378030799866"))