
# Criando a função media_lista, passando a variável lista como argumento
def media_lista(lista):
    total = sum(lista) # variavel de somar a lista
    media = total / len(lista) # criando uma variável para tirar a média da lista
    return media 

lista = [7.5, 8.0, 6.5, 9.0]
resultado = media_lista(lista)
print("A média dos valores da lista é:", resultado)
