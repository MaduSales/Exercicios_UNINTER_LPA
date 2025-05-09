# Escreva um algoritmo que obtenha do usuário uma frase de tamanho entre 10 e 30 caracteres. Faça a impressão dela na tela da maneira exata como foi digitada e, em seguida, remova os espaços da frase e imprima novamente, sem espaços.
frase = input('Digite uma frase de 10 a 30 caracteres: ')
tamanho = len(frase)

while tamanho < 10 or tamanho > 30:
  frase = input('Tente denovo, uma frase de 10 a 30 caracteres: ')
  tamanho = len(frase)

print(f'Frase com espaços: {frase}')
print(f'Frase sem espaços: ', end="")


for i in range(tamanho):
  if frase[i] != " ":
    print(frase[i], end='')
