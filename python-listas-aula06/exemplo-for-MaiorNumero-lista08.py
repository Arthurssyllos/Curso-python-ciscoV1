
# Criando uma lista de números
numeros = [10, 20, 30, 40, 50]

# Inicializando a variável que irá armazenar o maior número
maior_numero = numeros[0]

# Usando um loop for para percorrer a lista e encontrar o maior número
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

# Imprimindo o resultado
print('O maior número na lista é:', maior_numero)