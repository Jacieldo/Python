'''Manipulação de TEXTOS no python
tratando os textos'''
nome = 'Jacieldo da Silva Gonçalves'


#TAMANHO DA FRASE
len(nome)

#QUANTOS VEZES EXISTE O ELEMENTO "  "
nome.count('o',0 , 15)

nome.find('eld')

nome.find('calc')

#'jacieldo' in nome

nome.replace('Jacieldo', 'EU') #troca de palavras

nome.upper() #deixa tudo maiúsculo
nome.lower() #minusculo
nome.capitalize()
nome.title()
nome.strip() #remove espaço no começo e no final
nome.rstrip() #remove espaço da direita
nome.lstrip() #da esquerda
nome.split() #separa a frase por palavras. Cada palavra vira uma lista
'-'.join(nome) #vai colocar o '-' nos espaços

print(nome)
print(nome[5])
print(nome[2:6])
print(nome[: 10])
print(nome[0:15:2]) #pulando de 2 a 2
print(nome.count('a')) #é case sensitive


nome = nome.replace('Jacieldo', 'EU')
print(nome)
