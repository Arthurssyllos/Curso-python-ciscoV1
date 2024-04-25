# Criando um dicionario simples, com chave e valor (exemplo abaixo, 'cat' = chave, 'chat' = valor)
dicionario = {
    'cat':'chat',
    'dog':'chien',
    'horse':'cheval'
}

for chave in dicionario.keys(): # a função que usamos .keys é para varrer específico as chaves do dicionário
    print(chave, '->', dicionario[chave])