v1 = int(input('Digite um valor inteiro: '))
v2 = int(input('Digite outro número inteiro: '))

print('Observe o menu abaixo: ')
print('+ -> Adição')
print('- -> Subtração')
print('* -> Multiplicação')
print('/ -> Divisão')
print('** -> Potenciação')
op = input('Agora escolha qual operação deseja realizar: ')

if (op == '+'):
  print(v1 + v2)
elif (op == '-'):
  print(v1 - v2)
elif (op == '*'):
  print(v1 * v2)
elif (op == '/'):
  print(v1 / v2)
elif (op == '**'):
  print(v1 ** v2)
else:
  print('Inválido.')
