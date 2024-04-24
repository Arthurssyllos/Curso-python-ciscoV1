# Fazer uma função que ordene a lista abaixo (sem usar o sort): lista = [5, 2, 9, 1, 7]

def ordernar_lista(minha_lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista = [5, 2, 9, 1, 7]
lista_ordenada = ordernar_lista(lista)
print('A lista ordenada é:', lista_ordenada)

