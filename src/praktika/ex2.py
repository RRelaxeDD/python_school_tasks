def fib(n):
    num = 1
    next_num = 1
    with open("fib.txt", 'a+') as file:
        for _ in range(n):
            res = num + next_num
            num = next_num
            next_num = res
            file.write(f"{res}\n")


print(fib(200))

