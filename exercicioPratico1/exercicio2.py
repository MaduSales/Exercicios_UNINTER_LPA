kmPercorrido = int(input('Digite quantos km você percorreu com o carro alugado: '))

dias = int(input('Quantos dias você passou com o carro? '))

preco = (dias * 60) + (kmPercorrido * 0.15)

print(f'Você deverá pagar R${preco}')