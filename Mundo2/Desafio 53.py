print('----->DESAFIO 53<-----')
frase = input('Digite uma frase: ').strip().upper()#STRIP ELIMINA OS ESPAÇO ANTES E DEPOIS O UPPER DEIXA TUDO EM CAIXA ALTA
separado = frase.split() #SEPARA TODAS AS PALAVRAS
junto = ''.join(separado) #O ENTRE '' É A JUNÇÃO. ELIMINA OS ESPAÇOS ENTRE AS PALAVRAS

inverso =''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {} '.format(junto, inverso))

if inverso == junto:
    print('É um Palíndro!')
else:
    print('Não é um Palíndromo')