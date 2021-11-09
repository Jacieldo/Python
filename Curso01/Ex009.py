print('***DESAFFIO 022***')
nome = input('Digite o seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome.strip()) - nome.count(' '))
quebrado = nome.split()
print(len(quebrado[0])) #quantas letras tem o primeiro nome



print('***DESAFFIO 022***')
numero = int(input('Digite um número de 4 digitos: '))
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(numero // 1 % 10, numero // 10 % 10, numero // 100 % 10, numero // 1000 % 10))

print ('***DESAFIO 024***')
cidade = input('Qual a cidade que você nasceu: ').strip() #STRIP retira os espaços do início e do final
print(cidade[:5].upper() == 'SANTO') #Cidade vai do 0 ao 5 pois a palavra santo deve estar na primeira posição

print('***DESAFIO 025***')
nome25 = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome tem silva: {}'.format('SILVA' in nome25.upper()))

print('***DESAFIO 026***')
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {}x na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição: {}'.format(frase.rfind('A')+1))

print('***DESAFIO 027***')



