#Desafio para definir categoria de acordo com a idade
from datetime import date
print('-----> DESAFIO 41 <-----')

ano = int(input('Qual o ano do seu nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Nadador da categoria MIRIN!')
elif idade <= 14:
    print('Nadador da categoria INFANTIL!')
elif idade <= 19:
    print('Nadador da categoria JUNIOR!')
elif idade <= 20:
    print('Nadador da caregoria SẼNIOR!')
else:
    print('Nadador da catergoria MASTER!')
