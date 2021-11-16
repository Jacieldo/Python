from time import sleep

print('-----> DESAFIO 036 <-----')
print(' ')

valorCasa = float(input('Qual o valor da casa R$: '))
salario = float(input('Qual o seu salário mensal R$: '))
parcelas = int(input('Deseja pagar em quantos meses: '))
#Editando as cores do texto impresso na tela [style, text, back
print('\033[4:31m**Cálculos serão feitos desconsiderando juros de financiamento etc.\033[m')
print('Aguarde. Calculando...')
sleep(3)

prestacao = valorCasa / parcelas

if prestacao > (salario * 0.3):
    print('Negado. Divida em mais parcelas ou complemente a sua renda!')
    print('Suas prestações mensais não podem ultrapassar R$: {:.2f}'. format(salario * 0.3))
else:
    print('Sucesso. O emprestimo pode ser feito')
