print('-----> DESAFIO 43 <-----')
altura = float(input('Qual a sua altura: '))
peso = float(input('Qual o seu peso: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc <= 25:
    print('Você está no peso ideal!')
elif imc <= 30:
    print('Você está com sobre peso!')
elif imc <= 40:
    print('Seu Obeso')
else:
    print('Meu amigo, vá se tratar.')

