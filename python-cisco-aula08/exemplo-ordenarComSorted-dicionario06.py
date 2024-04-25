# Criando um dicionário simples de chave e valor
dicionario = {
    'horse':'cheval',
    'cat':'chat',
    'dog':'chien'
}

for chave in sorted(dicionario.keys()): # Usando o sorted para deixar em ordem alfabética, e o .keys() para pegar as chaves do dicionario
    print(chave, '->', dicionario[chave]) 