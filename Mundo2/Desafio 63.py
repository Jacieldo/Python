print('-----.DESAFIO 63<-----')
cont = int(input('Quantas termos deseja ver: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2),end='')

while cont >= 3:
    t3 = t1 + t2
    print(' -> {}'.format(t3),end='')
    cont -= 1
    t1 = t2
    t2 = t3