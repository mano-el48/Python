
def pa(a1, r, n):
    somaPa = 0
    
    for index in range(n):
        an = a1 + (r * index)
        print(f'a{index + 1} = {an}')
        somaPa += an
        
    return f'Soma pa = {somaPa}'

def pg(a1, q, n):
    somaPg = 0
    
    for index in range(n):
        an = a1 * (q ** index)
        print(f'a{index + 1} = {an}')
        somaPg += an
        
    return 'Soma pg = ' + str(somaPg)

#1, 2 e 5
a1 = int (input ('Digite o primeiro termo da Pa: '))
r = int (input ('Digite a razão: '))
n = int (input ('Digite o numero de termos da Pa: '))

a1 = int (input ('Digite o primeiro termo da Pg: '))
q = int (input ('Digite a razão: '))
n = int (input ('Digite o numero de termos da Pg: '))

print(pa(a1, r, n))

print('-' * 20)

print(pg(a1, q, n))