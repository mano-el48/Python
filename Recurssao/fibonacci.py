
def fibonacci(n):
    if (not n):#n == 0 
        return 0

    elif (n == 1):
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Informe o tamanho da sequencia: "))
print(fibonacci(n))
# for i in range(n):
#   print(fibonacci(i + 1))