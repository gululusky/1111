def fib(n):
    a,b=0,1
    for i in range(n):
        b,a=a+b,b
    return b
for i in range (0,100):
    print(fib(i))
print(fib(100)/fib(99))
