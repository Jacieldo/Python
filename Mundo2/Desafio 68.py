from random import randint
print('----->DESAFIO 68<-----')
print('JOGO DA PAR OU IMPAR')
vitorias = 0
while True:
    jogador = int(input('Digite um número inteiro: '))
    escolha =' '
    while escolha not in 'PI':
        escolha = str(input('Quer ser par ou impar:')).upper().strip()[0]
    pc = randint(0, 11)
    jogada = (jogador + pc) % 2
    if escolha == 'P':
        if jogada == 0:
            vitorias += 1
            print(f'Você escolheu {escolha} e o número {jogador} e o pc {pc}. O número {jogador + pc} é par. VITÓRIA')
        else:
            print(f'Você escolheu {escolha} e o número {jogador} e o pc {pc}. O número {jogador + pc} é impar. PERDEU')
            break
    else:
        if jogada != 0:
            vitorias += 1
            print(f'Você escolheu {escolha} e o número {jogador} e o pc {pc}. O número {jogador + pc} é par. VITÓRIA')
        else:
            print(f'Você escolheu {escolha} e o número {jogador} e o pc {pc}. O número {jogador + pc} é impar. PERDEU')
            break

print(f'Você ganhou {vitorias}vezes!')