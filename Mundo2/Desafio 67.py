print('----->DESAFIO 67<-----')
while True:
    num = int(input('Qual número deseja ver a tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {num} = {c*num}')
