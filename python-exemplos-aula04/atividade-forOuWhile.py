## Enunciados:

# 0 - Peça para  o usuário entrar com dois valores (primeiro e último).
# Faça a contagem entre esses números.
# Caso o último for menor que  o primeiro faça a contagem decrescente.
# Caso o último número for maior que o primeiro faça a contagem crescente.

# 1 - Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

# 2 - Faça um programa que peça ao usuário para adivinhar um número entre 1 e 100.
# Enquanto o número digitado não for igual a um número secreto definido pelo programa,
# o programa deve pedir ao usuário que tente novamente. Quando o usuário acertar o número,
# o programa deve imprimir "Parabéns, você acertou!".
# Use a biblioteca abaixo para números aleatórios:
# import random
# numero_secreto = random.randint(1, 100)

# 3 - Faça um programa que peça ao usuário para digitar uma sequência de números inteiros.
# O programa deve imprimir a soma dos números digitados, mas parar a soma se o usuário digitar um número negativo.

# 4 - Faça um programa que peça ao usuário para digitar o número de vezes que ele quer jogar uma moeda.
# O programa deve simular o lançamento de uma moeda e imprimir o resultado de cada lançamento (cara ou coroa).
# No final, o programa deve imprimir o número total de caras e o número total de coroas.
# Use a biblioteca abaixo para números aleatórios:
# import random
# resultado = random.randint(0, 1)

# 5 - Faça um programa que simule a urna eletrônica.
# A tela a ser apresentada deverá ser da seguinte forma:
# s opcoes sao:
# 1. Candidato Jair Rodrigues
# 2. Candidato Carlos Luz
# 3. Candidato Neves Rocha
# 4. Nulo
# 5. Branco
# Entre com o seu voto:
# O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes
# informações:
# a) O número de votos de cada candidato;
# b) A porcentagem de votos nulos;
# c) A porcentagem de votos brancos;
# d) O candidato vencedor.

# 6 - Faça um algoritmo em python capaz de realizar o cálculo de rentabilidade de uma poupança,
# esse algoritmo deve receber como entrada o valor inicial que o usuário está disposto a guardar.
# Como saída, o programa deve imprimir na tela mês a mês o montante por 12 meses
# aplicado a uma taxa de 0,5 % ao mês de rentabilidade.

# A fórmula do montante (M) de uma aplicação financeira é dada por:

# M = P * (1 + i)^n

# onde:

# P é o capital inicial (ou principal)
# i é a taxa de juros aplicada (em forma decimal) - divida o valor dado por 100
# n é o número de períodos de tempo em que o dinheiro ficará investido.

# 7 - Faça um programa que mostre o fatorial de um número fornecido pelo usuário.

## realização das atividads (código):

# 0 

def contar_numeros(primeiro, ultimo):
    if ultimo < primeiro:
        for i in range(primeiro, ultimo - 1, -1):
            print(i, end=' ')
    else:
        for i in range(primeiro, ultimo + 1):
            print(i, end=' ')

primeiro = int(input("Digite o primeiro número: "))
ultimo = int(input("Digite o último número: "))

print("Contagem:")
contar_numeros(primeiro, ultimo)

# 1

def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Pedir ao usuário para fornecer um valor entre 1 e 10
while True:
    valor = int(input("Digite um valor entre 1 e 10: "))
    if 1 <= valor <= 10:
        break
    else:
        print("Valor inválido. Tente novamente.")

# Exibir a tabuada do valor fornecido
print(f"Tabuada de {valor}:")
tabuada(valor)

# 2 

from random import randint
# Gerar número aleatório entre 1 e 100
numero_secreto = randint(1, 100)

# Loop para adivinhar o número
while True:
    # Solicitar ao usuário para adivinhar
    tentativa = int(input("Tente adivinhar o número entre 1 e 100: "))

    # Verificar se a tentativa é igual ao número secreto
    if tentativa == numero_secreto:
        print("Parabéns, você acertou!")
        break
    else:
        # Se a tentativa for incorreta, informar ao usuário e continuar o loop
        print("Tente novamente.")

# 3 

# Inicializar a soma
soma = 0

# Loop para solicitar os números e somá-los
while True:
    numero = int(input("Digite um número inteiro (digite um número negativo para parar): "))
    if numero < 0:
        break  # Encerra o loop se um número negativo for digitado
    soma += numero

# Imprimir a soma dos números digitados
print("A soma dos números digitados é:", soma)

# 4 

import random

# Inicializar contadores para caras e coroas
total_caras = 0
total_coroas = 0

# Pedir ao usuário para digitar o número de lançamentos da moeda
num_lancamentos = int(input("Digite o número de vezes que deseja lançar a moeda: "))

# Loop para simular os lançamentos e contar o número de caras e coroas
for _ in range(num_lancamentos):
    resultado = random.randint(0, 1)
    if resultado == 0:
        print("Cara")
        total_caras += 1
    else:
        print("Coroa")
        total_coroas += 1

# Imprimir o número total de caras e coroas
print("\nNúmero total de caras:", total_caras)
print("Número total de coroas:", total_coroas)

# 5 

def urna_eletronica():
    candidatos = {
        1: "Jair Rodrigues",
        2: "Carlos Luz",
        3: "Neves Rocha",
        4: "Nulo",
        5: "Branco"
    }

    total_votos = {candidato: 0 for candidato in candidatos.values()}
    total_votos_nulos = 0
    total_votos_brancos = 0

    while True:
        print("\nAs opções são:")
        for opcao, candidato in candidatos.items():
            print(f"{opcao}. Candidato {candidato}")

        print("6. Encerrar votação e apresentar resultados")

        voto = int(input("Entre com o seu voto: "))

        if voto == 6:
            print("\nResultado da votação:")
            for candidato, votos in total_votos.items():
                print(f"{candidato}: {votos} votos")

            percentual_nulos = (total_votos_nulos / sum(total_votos.values() + [total_votos_nulos + total_votos_brancos])) * 100
            percentual_brancos = (total_votos_brancos / sum(total_votos.values() + [total_votos_nulos + total_votos_brancos])) * 100

            print(f"Porcentagem de votos nulos: {percentual_nulos:.2f}%")
            print(f"Porcentagem de votos brancos: {percentual_brancos:.2f}%")

            vencedor = max(total_votos, key=total_votos.get)
            print(f"O candidato vencedor é: {candidatos[vencedor]}")
            break

        if voto in candidatos:
            total_votos[voto] += 1
        elif voto == 4:
            total_votos_nulos += 1
        elif voto == 5:
            total_votos_brancos += 1
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

urna_eletronica()

# 6

def calcular_rentabilidade_poupanca(valor_inicial):
    taxa_juros = 0.5 / 100  # Convertendo a taxa de juros para forma decimal
    montante = valor_inicial  # Montante inicial é igual ao valor inicial

    print("Mês\tMontante")
    for mes in range(1, 13):
        montante *= (1 + taxa_juros)  # Aplicando a fórmula do montante
        print(f"{mes}\t{montante:.2f}")

# Solicitar ao usuário o valor inicial
valor_inicial = float(input("Digite o valor inicial que você deseja guardar na poupança: "))

# Calcular e imprimir a rentabilidade ao longo de 12 meses
print("\nRentabilidade mensal ao longo de 12 meses:")
calcular_rentabilidade_poupanca(valor_inicial)

# 7 

def calcular_fatorial(numero):
    if numero < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

# Solicitar ao usuário para fornecer o número
numero = int(input("Digite um número para calcular o fatorial: "))

# Calcular e imprimir o fatorial do número fornecido
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")