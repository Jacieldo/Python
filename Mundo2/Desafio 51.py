print('----->DESAFIO 51<-----')
pt = int(input('Digite o primeiro termo da PA:'))
rz = int(input('DIgite a razão da PA: '))

pa = pt
print('Os 10 primeiros termos da PA são...')
for c in range(0, 10):
    pa += rz
    print(pa - rz)
