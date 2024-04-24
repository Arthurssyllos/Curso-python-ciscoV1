# Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.

minha_lista = []

num = int(input('Quantos elementos deseja? '))
for i in range(num):
     val = float(input('Entre com o número: '))
     minha_lista.append(val)
     maximo = max(minha_lista)
     minimo = min(minha_lista)

print('O elemento máximo da lista é:', maximo, '\nE o elemento mínimo da lista é:', minimo)