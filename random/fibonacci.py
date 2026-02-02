def fib(x):
    last = 1
    second_last = 1
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        for i in range(2, x+1):
            current = last + second_last
            second_last = last
            last = current
    
    return last
a = 15
print(fib(6))