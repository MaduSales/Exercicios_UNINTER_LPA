anoNascimento = int(input('Insira o seu ano de nascimento: '))
anoAtual = int(input('Digite o ano em que estamos: '))

idade = anoAtual - anoNascimento

if (idade > 18):
  print('Você já pode dirigir no Brasil com {} anos!' .format(idade))
else:
  print('Você ainda não pode dirigir no Brasil com {} anos...' .format(idade))
