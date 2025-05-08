# Escreva um algoritmo que repetidamente pergunte ao usuário qual sua idade e seu pronome. O programa deve encerrar quando o usuário digitar uma idade negativa.

while (idade > 0):
  idade = int(input('Qual a sua idade? '))
  pronome = input('Qual o seu pronome? ')

  if (pronome == 'ele' or pronome == 'Ele' or pronome == 'ELE'):
    print(f'Boa noite Senhor, sua idade é {idade}')
  
  elif (pronome == 'ela' or pronome == 'Ela' or pronome == 'ELA'):
    print(f'Boa noite Senhora, sua idade é {idade}')
  
  elif (pronome == 'elu' or pronome == 'Elu' or pronome == 'ELU'):
    print(f'Boa noite Senhore, sua idade é {idade}')
  
  else:
    print('Opção inválida.')

print('Idade negativa! Encerrando...')
