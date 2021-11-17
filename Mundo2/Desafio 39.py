#Desafio para contar a idade de apresentação nos serviços militares
from datetime import date

print('-----> DESAFIO 39 <-----')
ano = int(input('Em que ano você nasceu: '))
idade = date.today().year - ano

print(idade)

if idade < 17:
    print('Aind não está no prazo para se apresentar. Espere {} anos'.format(17 - idade))
elif idade == 17:
    print('Você está na idade para fazer o seu alistamento militar. Procure o posto próximo!')
else:
    print('Se você já fez o seu alistamento militar, OK. Se não, você está a {} anos atrasado'.format(idade - 17))
