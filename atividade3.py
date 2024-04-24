# Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, calcule a média dos números na lista.

# Criando uma lista

minha_lista = []

num = int(input('Quantos elementos deseja? '))
for i in range(num):
     val = float(input('Entre com o número: '))
     minha_lista.append(val)
     soma = sum(minha_lista)
     media = soma / len(minha_lista)

print(media)