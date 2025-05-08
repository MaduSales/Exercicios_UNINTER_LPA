# Escreva um algoritmo que calcule e exiba a tabuada de um número escolhido e digitado pelo usuário. A tabuada deve ser calculada até um determinado número n, também fornecido pelo usuário.
num = int(input('Digite um número que deseje saber a tabuada: '))
fim = int(input('Agora digite o limite da sua tabuada: '))
fim += 1

for i in range(fim):
  print(f'{num} X {i} = {num * i}')
