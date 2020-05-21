num = int(input('Digite um número: '))
print('-' * 12)
for mult in range(0,10):
    print('{0:0} x {1:2} = {2:0}'.format(num, mult, num*mult))
print('-' * 12)