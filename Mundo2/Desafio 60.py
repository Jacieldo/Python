print('----->DESAFIO 60<-----')
num = int(input('Digite um número inteiro: '))
fat = num

while num > 1:
    fat = fat * (num - 1)
    num -= 1
print(fat)