#Para importar toda a biblioteca (import ...)
#Quando se usa o import para importar toda a biblioteca, tem que usar o nome da biblioteca(.)item  **** raiz = math.sqrt(num)
#import math

import random

#Para importar apenas parte da biblioteca (from ... import ...)
#Quando se usa o from pra importar, não se usa o nome da biblioteca(.)o Item ****EX: raiz = sqrt(num)
from math import sqrt, floor,ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.3}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
print('')
num = random.random()
print(num)
print('')
num = random.randint(1, 15)
print(num)
