
# Criando uma lista
lista = [10, 1, 8, 3, 5]

# Inicializando a variável para armazenar a soma
soma = 0

# Usando um loop for para percorrer a lista e somar os elementos
for numero in lista:
    soma += numero

# Imprimindo a soma
print('A soma dos elementos da lista é:', soma)


## outra solução

minha_lista = [10, 1, 8, 3, 5] # Criando a lista
total = 0 # Declarado variável, iniciando com o valor zero

for i in range(len(minha_lista)):
    total += minha_lista[i]

print(total) # Imprimindo a variável total