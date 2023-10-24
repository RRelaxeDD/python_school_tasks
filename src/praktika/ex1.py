def fib(n):
    num = 1
    next_num = 1
    for _ in range(n):
        res = num + next_num
        num = next_num
        next_num = res
        yield res


print(list(fib(200)))

