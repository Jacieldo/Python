print('----->DESAFIO 55<-----')
peso = []

for c in range(0, 5):
    peso.append(float(input('Digite o peoso da {}° pessoa: '.format(c + 1))))

maior, menor = peso[0], peso[0]

for c in range(0, 5):
    if peso[c] > maior:
        maior = peso[c]
    elif peso[c] < menor:
        menor =peso[c]

print('O maior peso foi: {}kg e o menor foi: {}kg'.format(maior, menor))