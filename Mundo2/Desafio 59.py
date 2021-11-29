print('----->DESAFIO 59<------')
prim = float(input('Digite um valor: '))
seg = float(input('Digite outro valor: '))

op =0
while op != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair')
    op = int(input(''))

    if op == 1:
        print('A soma de {} + {} = {}'.format(prim, seg, prim + seg))
    elif op == 2:
        print('{} x {} = {}'.format(prim, seg, prim * seg))
    elif op == 3:
        if prim > seg:
            maior = prim
        else:
            maior = seg
        print('O maior número é o {}'.format(maior))
    elif op == 4:
        prim = float(input('Digite o novo primeiro número: '))
        seg = float(input('Digite o novo segundo número: '))
