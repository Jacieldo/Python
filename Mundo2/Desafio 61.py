print('----->DESAFIO 61<-----')
num = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Qual a razão da PA: '))

cont = 0

while cont < 10:
    num += rz
    print(num)
    cont += 1
