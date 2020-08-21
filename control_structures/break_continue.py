
for x in range(1, 10):
    if x % 2:
        continue
    print(x, end=' ')

print('\n')

for x in range(1, 10):
    if x % 2 == 0:
        continue
    print(x, end=' ')

print('\n')

for x in range(1, 10):
    if x == 5:
        break
    print(x, end=' ')

print('Fim!')
