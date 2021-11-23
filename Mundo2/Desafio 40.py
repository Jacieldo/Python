#Médio de notas de aluno
print('-----> DESAFIO 40 <-----')
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1 + nota2) / 2
print('MÉDIA: {:.2f}'.format(media))

if media < 5:
    print('Aluno REPROVADO!')
if media < 7:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('Aluno APROVADO!')

