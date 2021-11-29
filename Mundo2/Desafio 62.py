print('----->DEAFIO 62<-----')

num = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Qual a razão da PA: '))

cont = 0

while cont < 10:
    num += rz
    print(num)
    cont += 1

mais = 1
while mais != 0:
    mais = int(input('Deseja ver mais quantos termos: '))
    while cont < 10 + mais:
        num += rz
        print(num)
        cont += 1
    cont = 10