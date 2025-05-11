# 1º bacon() é chamado e possui 6 ovos. Dentro de bacon(), é chamado omelete() com 12 ovos. Após isso, bacon() exibe novamente 6 ovos. 
# Por fim, a variável global é exibida na tela

def omelete():
  ovos = 12
  print('Ovos = ', ovos)

def bacon():
  ovos = 6
  print('Ovos = ', ovos)
  omelete()
  print('Ovos = ', ovos)

ovos = 2
bacon()
print('Ovos = ', ovos)
