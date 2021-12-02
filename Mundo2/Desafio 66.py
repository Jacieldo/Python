print('----->DESAFIO 66<-----')
cont = soma = 0
while True:
    num = int(input('Digite um número. [999 para terminar]: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Você digitou {cont} números e a soma foi {soma}')