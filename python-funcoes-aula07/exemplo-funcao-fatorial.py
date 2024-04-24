
# Criando a função e recebendo a variável numero como argumento
def calcular_fatorial(numero):
    if numero == 0: # enquanto o numero (variável) não for zero entrará no if (loop)
        return 1
    else:
        return numero * calcular_fatorial(numero-1) # neste caso, ele irá fazer 5 * (5 - 1) = 5 * 4...
    
numero = 5
fatorial = calcular_fatorial(numero)
print('O fatorial de', numero, 'é', fatorial)