print('----->DESAFIO 48<-----')
print('Vou te mostrar a soma de todos os números impares múltiplos de 3 que estão no intervalo de 1 a 500!')
soma = 0
for c in range(0, 501):
    if c > 0 and c % 2 != 0  and c % 3 == 0:
        soma += c
print(soma)
