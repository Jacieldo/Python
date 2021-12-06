i: int = 5
n = ' DESAFIO{:^3} '.format(i)
print('{:*^20} \n'.format(n))
i = i+1
num = int(input('Digite um número inteiro: '))
print('O número anterior é {} e o sucessor é {}\n'.format(num-1, num+1))


n = ' DESAFIO{:^3} '.format(i)
print('{:*^20}'.format(n))
i = i+1
num2 = int(input("Digite um número: "))
print('O dobro é: {} \nO Triplo é: {} \nA raiz quadrada é: {:.2}\n'.format(num2*2, num2*3, num2**(1/2)))

n = ' DESAFIO{:^3} '.format(i)
print('{:*^20}'.format(n))
i = i + 1
n1 = float(input('Digite a primeiro nota: '))
n2 = float(input('Digite a segunda nota: '))
print("A média do aluno é: {:.2f}".format((n1+n2)/2))
print('')


n = ' DESAFIO{:^3} '.format(i)
print('{:*^20}'.format(n))
i = i + 1
metros = float(input('Digite um valor em metros: '))
print('{}m é igual a {}cm e {}mm'.format(metros, metros*100, metros*1000))
print('')


#Desafio 009
n = ' DESAFIO{:^3} '.format(i)
print('{:*^20}'.format(n))
i = i + 1
tabuada = int(input('Digite um número inteiro: '))
for contT in range(1, 11):
    print('{} x {} = {}'.format(tabuada, contT, tabuada*contT))


n = ' DESAFIO{:^3} '.format(i)
print('{:*^20}'.format(n))
i = i + 1
dinheiro = float(input('Quantos reais tu tens na carteira: '))
print('Você pode comprar US${:.2f}'.format(dinheiro/5.43))
print('')


n = ' DESAFIO{:^3} '.format(i)
print('{:*^20}'.format(n))
i = i + 1
print('Digite as dimensões da parede!!!')
largura = float(input('Largura: '))
altura = float(input('Altura: '))
print('A parede tem {}m² e e precisara de {}litros para pinta-la'.format(altura*largura, (altura*largura)/2))
print('')


n = ' DESAFIO{:^3} '.format(i)
print('{:*^20}'.format(n))
i = i + 1
produto = float(input('Digite o preço do produto: '))
print('O produto teve um desconto de 5% e o seu novo preço é R${:.2f}'.format(produto*0.95))
print('')

n = ' DESAFIO{:^3} '.format(i)
print('{:*^20}'.format(n))
i = i + 1
salario = float(input('Quanto você ganha: '))
print('Seu novo sálario com 15% de reajuste é R${:.2f}' .format(salario*1.15))
print('')

n = ' DESAFIO{:^3} '.format(i)
print('{:*^20}'.format(n))
i = 15
km = float(input('Quantos kms foram rodados: '))
dias = int(input('Quantos dias de aluguel: '))
print('O valor a ser pago é R$ {:.2f}'.format((dias*60)+(km*0.15)))
