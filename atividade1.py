# Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, imprima apenas os números pares da lista.

minha_lista = []

num = int(input('Quantos elementos deseja? '))
for i in range(num):
     val = float(input('Entre com o número: '))
     minha_lista.append(val)

print("Números pares da lista:")
for num in minha_lista:
    if num % 2 == 0:
        print(num)