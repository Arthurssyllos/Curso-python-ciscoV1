# Criando uma lista
minha_lista = [10, 1, 8, 3, 5]

print(minha_lista) # Imprimindo a lista antes das trocas (ou modificações)

minha_lista[0], minha_lista[4] = minha_lista[4], minha_lista[0] # trocando os índices de lugar, trocando o 0 para 4, e 4 para 0
minha_lista[1], minha_lista[3] = minha_lista[3], minha_lista[1] # trocando o índice 1 pelo 3 e o 3 pelo 1

print(minha_lista)