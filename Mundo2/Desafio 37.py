print('-----> Desafio 037 <-----')
print('CALCULADORA DE CONVERSÃO DE BASE')
print(' ')

num = int(input('Digite um número inteiro: '))
print('PARA QUAL BASE DESEJA TRANSFORMAR?')
print('[1] - para binário')
print('[2] - para octal')
print('[3] - para hexadecimal')
op = int(input('Opção: '))

if op == 1:
    print('O número {} na base BINÁRIA é: {}'.format(num, bin(num)[2:]) ) #Fatiamento de string (tratamento de string)
elif op == 2:
    print('O número {} na base OCTAL é: {}'.format(num,oct(num)[2:])) #Fatiamento de string
elif op == 3:
    print('O número {} na base HEXIDECIMAL é: {}'.format(num, hex(num)[2:])) #Fatiamento de string (AULA 10 - CURSO 01)
else:
    print('Opção INVÁLIDA. Tente novamente')

