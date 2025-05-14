# Escreva uma rotina que recebe três valores como parâmetro e coloque-os em ordem crescente, ou seja, o menor ao maior.
def recebeValor():
  print('Olá! Digite três números para saber a ordem crescente entre eles!')
  val1 = int(input('Digite o primeiro número: '))
  while val1 < 0:
    val1 = int(input('Inválido! Digite o primeiro número para continuar: '))

  val2 = int(input('Digite o segundo número: '))
  while val2 < 0:
    val2 = int(input('Inválido! Digite o segundo número para continuar: '))
    
  val3 = int(input('Digite o último número: '))
  while val3 < 0:
    val3 = int(input('Inválido! Digite o último número para continuar: '))

  comparaValor(val1, val2, val3)

def comparaValor(val1, val2, val3):
  if (val1 < val2) and (val1 < val3):
    if (val2 < val3):
      print('Ordem crescente: {}, {}, {}'.format(val1, val2, val3))
    else:
      print('Ordem crescente: {}, {}, {}'.format(val1, val3, val2))
  elif (val2 < val1) and (val2 < val3):
    if (val1 < val3):
      print('Ordem crescente: {}, {}, {}'.format(val2, val1, val3))
    else:
      print('Ordem crescente: {}, {}, {}'.format(val2, val3, val1))
  elif (val3 < val1) and (val3 < val2):
    if (val1 < val2):
      print('Ordem crescente: {}, {}, {}'.format(val3, val1, val2))
    else:
      print('Ordem crescente: {}, {}, {}'.format(val3, val2, val1))
  else: 
    print('Todos os números são iguais!')
  
recebeValor()
