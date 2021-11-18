print('-----> DESAFIO 44 <-----')

produto = float(input('Qual o preço do produto: '))

print('***Escolha forma de pagamento***')
print('1 - A vista dinheiro ou cheque')
print('2 - A Vista no cartao')
print('3 - Parcelado no cartao em ate 2x')
print('4 - Parcelado no cartao em 3x')
op = int(input(''))

if op == 1:
    produto = produto * 0.9
elif op == 2:
    produto = produto * 0.95
elif op == 3:
    produto = produto
elif op == 4:
    produto = produto * 1.2
else:
    print('Opçao invalida. Tente novamente!')

print('O preço do produto ficará R$ {:.2f}'.format(produto))

