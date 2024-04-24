# Criando uma lista, para ordenar
minha_lista = [17, 8, 10, 6, 2, 4 ]
trocado = True # Precisamos dele para entrar no loop While

while trocado:
     trocado = False # sem trocas até agora
     for i in range(len(minha_lista) -1):
          if minha_lista[i] > minha_lista[i + 1]:
               trocado = True # ocorreu uma troca!
               minha_lista[i], minha_lista[i + 1] = minha_lista[i + 1], minha_lista[i]

print(minha_lista)