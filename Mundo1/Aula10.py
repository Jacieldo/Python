import random
from datetime import date
print('***DESAFIO 028***')
print('Eu pensei em um número Inteiro entre 0 e 5!!!')
num1 = random.randint(0 , 5)
num2 = int(input('Tente acertar o número que eu pensei: '))
if num1 == num2:
    print('Isso mesmo. Você acertou o número que eu pensei!!!')
else:
    print('Você errou. O núemero que eu pensei foi: {}'.format(num1))


print('***DESAFIO 029***')
velocidade = float(input('Qual a sua velocidade: '))
if velocidade > 80:
    print('Você foi multado em R$ {}'.format((velocidade - 80) * 7))
else:
    print('Mantenha sua velocidade em até 80km para não ser multado!!!')

print('***DESAFIO 030***')
num3 = int(input('Digite um número inteiro: '))
if (num3 % 2) == 0:
    print('O número {} é PAR!!!'.format(num3))
else:
    print('O número {} é IMPAR!!!'.format(num3))



print('***DESAFIO 031***')
distancia = int(input('Quantos KM(inteiro) terá a sua viagem: '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('O custo da sua viagem será de \033[1;34;45m R$ {:.2f}\033[m'.format(valor))



print('***DESAFIO 032***')
ano = int(input('Digite um ano para saber se ele é bissexto: '))
if ano == 0:
    ano = date.today().year
if (ano % 4) == 0:
    if (ano % 100) == 0:
        if (ano % 400) == 0:
            print('O ano {} não é um ano bissexto!'.format(ano))
        else:
            print('O ano {} não é bissexto!!!'.format(ano))
    else:
        print('O ano {} é um ano bissexto!!!'.format(ano))
else:
    print('{} não é um ano bissexto!!!'.format(ano))





print('***DESAFIO 033***')
num4 = int(input('Digite o primeiro número: '))
num5 = int(input('Digite o segundo número: '))
num6 = int(input('Digite o terceiro número: '))
if num4 > num5:
    if num4 > num6:
        if num5 > num6:
            print('O maior número é {} e o menor é {}'.format(num4, num6))
        else:
            print('O maior número é {} e o menor é {}'.format(num4, num5))
    else:
        print('O maior número é {} e o menor é {}'.format(num6, num5))
elif num5 > num6:
    if num6 > num4:
        print('O maior número é {} e o menor é o {}'.format(num5, num4))
    else:
        print('O maior número é {} e o menor é o {}'.format(num5, num6))
else:
    print('O maior núme e o {} e o menor e o {}'.format(num6, num4))




print('***DESAFIO 034***')
salario = float(input('Qual o valor do seu salario atual: R$ '))
if salario > 1250:
    salario += salario * 0.1
else:
    salario += salario *0.15
print('Seu novo salario e de R$ {:.2f}'.format(salario))

print('***DESAFIO 035***')
l1 = int(input('Digite o primeiro lado do triangulo: '))
l2 = int(input('Digite o segundo lado do triangulo: '))
l3 = int(input('Digite o terceiro lado do triangulo: '))
#TESTE 01
if (l2 - l3) < 0:
    m1 = (l2 - l3) * (-1)
else:
    m1 = (l2 - l3)
t1 = (m1 < l1) and (l1 < (l2 + l3))
print(t1)

#TESTE 02
if (l1 - l3) < 0:
    m2 = (l1 - l3) * (-1)
else:
    m2 = (l1 - l3)
t2 = (m2 < l2) and (l2 < (l1 + l3))
print(t2)

#TESTE 03
if (l1 - l2) < 0:
    m3 = (l1 - l2) * (-1)
else:
    m3 = (l1 - l2)
t3 = (m3 < l3) and (l3 < (l1 + l2))
print(t3)

if (t1 == False) or (t2 == False) or (t3 == False):
    print('Não é possível formar um triangulo!!!')
else:
    print('É possível formar um triangulo!!!')



