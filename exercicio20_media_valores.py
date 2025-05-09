# Faça a média de valores positivos e inteiros.

soma = 0
qtd = 0
media = 0

while True:
  x = int(input('Digite um valor positivo e inteiro: '))

  if x < 0:
    continue
  if not x: 
    break

  soma += x
  qtd += 1

media = soma / qtd

print(media)
