preco = float(input('Insira o preço de um produto: '))
percentual = float(input('Agora insira o percentual a ser aplicado no produto: '))

desconto = preco * (percentual / 100)
precoFinal = preco - desconto

print(f'O preço total era R${preco}, mas com um desconto de {desconto}%, o preço saiu por R${precoFinal}')