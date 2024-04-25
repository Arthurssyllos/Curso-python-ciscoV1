# Criando um dicionário simples com chave e valor, respectivamente, o valor como visto não é do tipo string
products = {
    'banana': 2.50,
    'maçã': 3.00,
    'laranja': 2.75,
    'abacaxi': 4.50,
    'manga': 3.50
}

# Imprimir o preço de uma maça
print(' O preço de uma maçâ é: R$' + str(products['maçã'])) # Alterando o tipo para string, para realizar a concatenação, de str + str

# Adicionando um novo produto
products['melancia'] = 6.00 # Sempre obedecendo a regra de [chave] = valor, nesse caso o valor não é do tipo str(string)

# Imprimir todos os produtos e seus preços
for product, price in products.items():
    print(product + ': R$' + str(price))