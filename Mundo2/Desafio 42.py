print('-----> DESAFIO 42 <-----')
l1 = int(input('Digite o primeiro lado do triangulo: '))
l2 = int(input('Digite o segundo lado do triangulo: '))
l3 = int(input('Digite o terceiro lado do triangulo: '))
#TESTE 01
if (l2 - l3) < 0:
    m1 = (l2 - l3) * (-1)
else:
    m1 = (l2 - l3)
t1 = (m1 < l1) and (l1 < (l2 + l3))

#TESTE 02
if (l1 - l3) < 0:
    m2 = (l1 - l3) * (-1)
else:
    m2 = (l1 - l3)
t2 = (m2 < l2) and (l2 < (l1 + l3))

#TESTE 03
if (l1 - l2) < 0:
    m3 = (l1 - l2) * (-1)
else:
    m3 = (l1 - l2)
t3 = (m3 < l3) and (l3 < (l1 + l2))

if (t1 == False) or (t2 == False) or (t3 == False):
    print('Não é possível formar um triangulo!!!')

else:
    if (t1 == t2 and t1 != t3) or (t1 == t3 and t1 != t2) or (t2 == t3 and t1 != t2):
        print('O trinangulo é ISÓCELES!')
    elif (t1 != t2) and (t1 != t3) and (t2 != t3):
        print('O trinangulo é ESCALENO!')
    elif (t1 == t2) and (t2 == t3):
        print('O triangulo é Equilátero!')
    else:
        print('Não seria possível existir essa condição!')
