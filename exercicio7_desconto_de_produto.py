# Composição Moderna
preco = float(input('Insira o preço de um produto: '))
percentual = float(input('Agora digite o percentual para aplicar desconto: '))

desconto = preco * (percentual / 100)
total = preco - desconto

print('O preço do produto é R${}, porém, com um desconto de {}%, o preço saiu por R${}' .format(preco, desconto, total))
