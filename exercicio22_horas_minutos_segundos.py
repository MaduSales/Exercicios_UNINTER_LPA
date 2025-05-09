# Escreva um algoritmo que imprima na tela as horas no formato H:M:S dentro de um intervalo definido pelo usuário. O usuário deverá delimitar o intervalo de horas que deseja imprimir (por exemplo, das 7h até as 14h).
horaInicial = int(input('Digite um horário para começar: '))
horaFinal = int(input('Digite um horário para finalizar: '))

while horaInicial > horaFinal or horaInicial < 0 or horaFinal > 23:
  horaInicial = int(input('Inválido. Tente de novo. Digite um horário para começar: '))
  horaFinal = int(input('Digite um horário para finalizar: '))

for horas in range(horaInicial, horaFinal + 1):
  for minutos in range(60):
    for segundos in range(60):
      print(f'{horas}:{minutos}:{segundos}')
      if horas == horaFinal and segundos == 0:
        break
    if horas == horaFinal and minutos == 0:
      break
  if horas == horaFinal:
    break 
