# Criando um dicionário, porém em uma forma melhor e mais visível (tem a opção 1, que seria dicionario = {'chave':'valor', 'chave':'valor'})
dicionario = {
    'gato':'chat',
    'dog':'chien',
    'cavalo':'cheval'
}

palavras = ['gato', 'lion', 'cavalo'] # Criando uma lista, com nomes de animais

for palavra in palavras: # Fazendo um For, para varrer a lista (palavras) e a palavra se tiver em dicionário, Imprima (print) a palavra (da lista) e o valor que está no dicionário
    if palavra in dicionario:
        print(palavra, '- >', dicionario[palavra])
    else:
        print(palavra, 'Não está no dicionário')