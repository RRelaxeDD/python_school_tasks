class MyDecorators:

    @staticmethod
    def check_alpha(func):

        def inner(arg: str):
            
            for i in arg:
                if not i.isalpha():
                    print("not all chars are letter")
                    return
            func(arg)
        
        return inner
    
    @staticmethod
    def check_numbers(func):

        def inner(arg: str):

            for i in arg:
                if not i.isdigit():
                    print("not all chars are int")
                    return
            func(arg)    
        
        return inner



@MyDecorators.check_alpha
def print_if_all_letters(sentence):
    print(sentence)

@MyDecorators.check_numbers
def print_if_all_ints(sentence):
    print(int(sentence[0]))


print_if_all_letters("fnjasbdiuaoaiufiajw")
print_if_all_letters("fnjasbdiuaoaiufiajw1")

print_if_all_ints("385139740828")
print_if_all_ints("385139740828a")