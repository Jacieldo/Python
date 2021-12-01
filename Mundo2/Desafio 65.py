print('----->DESAFIO 65<-----')

cont = 1
maior = 0
num = int(input('Digite um número inteiro: '))
soma = num
menor = num
continuar = str(input('Deseja continuar(s/n)? '))
if continuar == 'n':
    print('Os números são iguais e a média é o próprio número.')
elif continuar == 's':
    while continuar == 's':
        num = int(input('Digite outro número inteiro: '))
        cont += 1
        soma += num
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        continuar = str(input('Deseja continuar(s/n)? '))
    print('O maior número digitado foi: {}'.format(maior))
    print('O menor número digitado foi: {}'.format(menor))
    print('A média dos números é: {}'.format(soma / cont))
else:
    print('Error. Esperava-se um valor validos!')
