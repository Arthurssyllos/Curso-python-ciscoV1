# Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima a lista com os números duplicados removidos.

# Criando uma lista, para ordenar

minha_lista = []

trocado = True # Precisamos dele para entrar no loop While

num = int(input('Quantos elementos deseja? '))
for i in range(num):
     val = float(input('Entre com o número: '))
     minha_lista.append(val)

while trocado:
     trocado = False # sem trocas até agora
     for i in range(len(minha_lista) -1):
          if minha_lista[i] > minha_lista[i + 1]:
               trocado = True # ocorreu uma troca!
               minha_lista[i], minha_lista[i + 1] = minha_lista[i + 1], minha_lista[i]

print('\nOrdenado:')