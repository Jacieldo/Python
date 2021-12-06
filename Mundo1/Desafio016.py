from math import floor, sqrt, trunc, radians, sin, cos, tan
import random
import pygame


print('***Desafio 015***')
num = float(input('Digite um número real: '))
print('A parte inteira de {} é {}, {}'.format(num, floor(num), trunc(num)))




print('***Desafo 016***')
oposto = float(input('Digite o valor do Cateto Oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipo = (oposto**2 + adjacente**2)
print('O valor da hipotenusa é: {:.4}'.format(sqrt(hipo)))
print('')



print('***Desafio 017***')
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print('O seno de {} é {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O cosseno de {} é {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('A tangente de {} é {:.2f}'.format(angulo, tangente))
print('')

print('***Desafio 018***')
listaNome = []
for i in range(4):
    nomes = input('Digite o nome do aluno {} '.format(i+1))
    listaNome.append(nomes)

sorteio = random.randint(1, 4)
print('O aluno sorteado foi: {}'.format(listaNome[sorteio]))




print('***Desafio 019***')
listaNome = []
for i in range(4):
    nomes = input('Digite o nome do aluno {} '.format(i + 1))
    listaNome.append(nomes)

sorteio = random.randint(1, 4)
print('O aluno sorteado foi: {}'.format(listaNome[sorteio]))
print('')



print('***Desafio 020***')
nome = [4]
for i in range(4):
    a = input('{}° aluno: '.format(i + 1))
    nome.append(a)

print('A ordem dos alunos sorteados foi:')
for i in range(4):
    b = random.randint(1 ,4-i)
    print(nome[b])
    del(nome[b])


print('***Desafio 021***  TOCAR MÚSICA MP3')
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()