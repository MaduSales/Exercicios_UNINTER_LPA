# Escreva um algoritmo que calcule a média dos números pares de 1 até 100 (1 e 100 inclusos). Implemente o laço usando for.
soma = 0
qtd = 0
for i in range(1, 101):
  if i % 2 == 0:
    soma += i
    qtd += i

media = soma / qtd
print(media)
