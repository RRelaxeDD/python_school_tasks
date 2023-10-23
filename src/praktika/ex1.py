import time

def exec_time(func):

    def inner():
        start = time.time()
        func()
        end = time.time() - start
        print(f"\ntime of excecution is {end} seconds")
    
    return inner

@exec_time
def fibonacci(): 
    fib1 = fib2 = 1 
 
    for i in range(2, 200): 
        fib1, fib2 = fib2, fib1 + fib2 
        print(fib2, end=' ') 
 
 
if __name__ == '__main__': 
    fibonacci()