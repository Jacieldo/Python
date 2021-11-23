print('----->DESFIO 50<-----')

numeros = []
for c in range(0, 6):
    numeros.append(int(input('Digite o {}° número: '.format(c + 1))))

par = []
for a in range(0, 6):
    if (numeros[a]) % 2 == 0:
        par.append(numeros[a])

cont = (len(par))
soma = 0
if cont != 0:
    for b in range(0, cont):
        soma += par[b]
    print('A soma dos números pares é {}'.format(soma))
else:
    print('Não foi digitado nenhum número par!!')


