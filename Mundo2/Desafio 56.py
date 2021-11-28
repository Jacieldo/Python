print('----->Desafio 56<-----')
mediaIdade = 0
maiorIdade = 0
contMulheres = 0

for cl in range(0, 4):
    print('Dados da {}° pessoa:'.format(cl +1))
    for cc in range(0, 3):
        if cc == 0:
           nome = input('Digite seu nome: ')
        elif cc == 1:
            idade = int(input('Qual a sua idade: '))
            mediaIdade += idade
        else:
            sexo = input('Sexo: ')
            if sexo == 'masculino':
                if maiorIdade < idade:
                    maiorIdade = idade
                    nomeVelho = nome
            elif sexo == 'feminino':
                if idade < 20:
                    contMulheres += 1




print('A média de idade é {:.2f},'.format(mediaIdade / 4))
print('O homem mais velho se chama: {}'.format(nomeVelho))
if contMulheres > 0:
    print('{} tem menos de 20 anos'.format(contMulheres))
else:
    print('Não tem mulheres na lista ou nenhuma tem menos de 20 anos')
            
