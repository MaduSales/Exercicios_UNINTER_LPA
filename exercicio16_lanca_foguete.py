# Crie um algoritmo para exibir na tela uma contagem regressiva do lançamento de um foguete, iniciando em 10 até 0, e escrevendo após o 0, a palavra: Fogo!
for i in range(10, -1, -1):
  print(i)
  if i < 1:
    print('Fogo!')
