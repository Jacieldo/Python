print('----->DESAFIO 57<-----')

sexo = str(input('Qual o o seu sexo: ')).strip().upper()[0]#STRIP - Elimina os espaços o UPPER -  deixa tudo maiúsculo
#O [0] é pra pegar só a primeira letra
while sexo != 'F' and sexo !='M':
    print('Erro. Digite m para masculino ou f para feminino:')
    sexo = str(input('')).strip().upper()[0]