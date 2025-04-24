# Composição Moderna
dias = int(input('Quantos dias? '))
horas = int(input('Quantos horas? '))
minutos = int(input('Quantos minutos? '))
segundos = int(input('Quantos segundos? '))

# 1 dia = 24h | 1h = 60min | 1min = 1seg
total = segundos + (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

print('O total de segundos de {} dias, {} horas, {} minutos e {} segundos é: {} segundos' . format(dias, horas, minutos, segundos, total))

# Composição Simples
dias = int(input('Quantos dias? '))
horas = int(input('Quantos horas? '))
minutos = int(input('Quantos minutos? '))
segundos = int(input('Quantos segundos? '))

# 1 dia = 24h | 1h = 60min | 1min = 1seg
total = segundos + (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

print('O total de segundos de %i dias, %i horas, %i minutos e %i segundos é: %i segundos' % (dias, horas, minutos, segundos, total))
