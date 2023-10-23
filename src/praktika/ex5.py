class FirstChartNotIntException(Exception):
    pass

def some_function(arg):

    if not arg[0].isdigit():
        raise FirstChartNotIntException("first char must be int")
    
    print("all ok go next")

some_function("7361 7420 6869")
some_function("a7361 7420 6869")