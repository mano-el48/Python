
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


print(pa(1, 2, 5))

print('-' * 20)

print(pg(1, 2, 5))