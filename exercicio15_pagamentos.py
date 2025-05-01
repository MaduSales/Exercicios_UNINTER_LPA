print('PAGAMENTO')
print('1 - à vista')
print('2 - parcelado em 3x')
print('3 - parcelado em 5x')
print('4 - parcelado em 10x')

op = int(input('Qual seria a forma de pagamento? '))
valor = float(input('Digite o valor da compra: '))

if (op == 1):
  desconto = valor * (5/100)
  valor_final = valor - desconto
  print(f'O produto foi comprado à vista no valor de R${valor_final:.2f} com um desconto de R${desconto:.2f}')
elif (op == 2):
  valor_final = valor 
  parcela = valor_final / 3
  print(f'O produto foi parcelado em 3x de R${parcela:.2f}, sendo o valor total da compra R${valor_final:.2f}')
elif (op == 3):
  acrescimo = valor * (2/100)
  valor_final = valor + acrescimo
  parcela = valor_final / 5
  print(f'O produto foi parcelado em 5x de R${parcela:.2f}, sendo o valor total da compra R${valor_final:.2f} por conta do acréscimo de 2%')
elif (op == 4):
  acrescimo = valor * (8/100)
  valor_final = valor + acrescimo
  parcela = valor_final / 10
  print(f'O produto foi parcelado em 10x de R${parcela:.2f}, sendo o valor total da compra R${valor_final:.2f} por conta do acréscimo de 8%')
