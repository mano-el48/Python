def fib(n):
    if (not n):#n == 0 
        return 0

    elif (n == 1):
        return 1
    
    return fib(n - 1) + fib(n - 2)

n = int(input("Informe o tamanho da sequencia: "))
print(fib(n))
# for i in range(n):
#   print(fib(i + 1))