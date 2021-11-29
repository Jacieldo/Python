from datetime import date
print('----->DESAFIO 54<-----')
maior = 0
menor =0

for c in range(0, 7):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = date.today().year - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('{} pessoas maiores de idade e {} menores de idade!'.format(maior, menor))
