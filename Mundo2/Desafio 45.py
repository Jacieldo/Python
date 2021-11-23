#Jogando Jokenpô com o computador
import random
print('-----> DESAFIO 45 <-----')

print('***Escolha a sua opção:***')
print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')
jogador = int(input(''))

pc = random.randint(1,3)

if jogador == 1:
    if pc == 1:
        print('Ninguém ganhou!')
    elif pc == 2:
        print('O computador ganhou!')
    else:
        print('Você ganhou!')

if jogador == 2:
    if pc == 1:
        print('Você ganhou!')
    elif pc == 2:
        print('Ninguém ganhou!')
    else:
        print('O computador ganhou!')

if jogador == 3:
    if pc == 1:
        print('O computador ganhou!')
    elif pc == 2:
        print('VOcê ganhou!')
    else:
        print('Nonguém ganhou!')

print('Você escolheu {} e o computador {}'.format(jogador, pc))
