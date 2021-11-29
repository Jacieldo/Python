import random
print('----->DESAFIO 58<-----')
pc = random.randint(0, 10)
sorte = int(input('Digite um número inteiro: '))
print(pc)
cont = 0
if pc != sorte:
    while pc != sorte:
        sorte = int(input('Tente novamente: '))
        cont += 1

print('Foram feitas {} tentativas'.format(cont + 1))