
# Criando uma função
def lista_soma(lst):
    s = 0 # Definindo a variável s, que começa com 0
    for elem in lst:
        s += elem
    return s

print(lista_soma([5, 4, 3]))