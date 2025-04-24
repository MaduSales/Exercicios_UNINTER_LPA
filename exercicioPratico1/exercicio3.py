frase1 = input('Digite uma frase qualquer: ')

tamanho = len(frase1)
frase2 = frase1[:int(tamanho/2)]

print(frase2[-2:])