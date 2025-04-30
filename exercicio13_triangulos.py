A = int(input('Digite um lado de um triângulo para descobrir seu tipo: '))
B = int(input('Digite o outro lado: '))
C = int(input('Insira o último lado: '))

if (A > 0 and B > 0 and C > 0):
  if (A + B > C and B + C > A and A + C > B):
    if (A == B and A == C and B == C):
      print('Esse é um Triângulo Equilátero!')
    else:
      if (A != B and A != C and B != C):
       print('Esse é um Triângulo Escaleno!')
      else: 
        print('Esse é um Triângulo Isósceles!')
  else:
    print('Aparentemente há um lado desproporcional neste "triângulo". Tente usar medias menores!')
else:
  print('Nenhum lado pode ser zero em um triângulo.')
