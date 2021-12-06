print('***DESAFIO 031***')
distancia = int(input('Quantos KM(inteiro) terá a sua viagem: '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('O custo da sua viagem será de \033[1;34;45m R$ {:.2f}\033[m'.format(valor))