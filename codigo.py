def Calcular_Media (notas):
 
  soma = sum(notas)
  quantidade = len(notas)
  media = soma/quantidade

  if(media<5):
    print(f'Sua media foi {media:.2f}')
    print('Reprovado')
    
  elif(media>=5 and media<=10):
    print(f'Sua media foi {media:.2f}')
    print('Aprovado')
  else:
    print('Nota Invalida')

nota = -1
somageral = []
while nota!=0:
  nota = float(input('Digite uma nota ou zero para sair : '))
  somageral.append(nota)
  

Calcular_Media(somageral)


