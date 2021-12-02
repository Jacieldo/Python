print('----->DESAFIO 64<-----')
cont = soma = 0
num = int(input('Digite um número inteiro: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro: '))

print('A soma foi: {} e você digitou {} númeoros'.format(soma, cont))