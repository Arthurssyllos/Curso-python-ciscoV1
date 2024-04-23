# armazena um número pequeno
maior_numero = -999999999
# entra com o primeiro número
number = int(input('Entre com um número ou digite -1 para parar: '))
# se o numero nao for igual a -1 continua
while number != -1:
    # O numero é maior que o maior_numero
    if number > maior_numero:
        # SIm, atualiza maior_numero
        maior_numero = number
    # Entre com o próximo número
    number = int(input('Entre com um número ou digite -1 para parar: '))
# Print o maior número
print('O maior número é: ', maior_numero)