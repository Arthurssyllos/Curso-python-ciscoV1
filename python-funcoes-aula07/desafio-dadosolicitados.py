# Fazer uma função que conte de 1 até 100, fazer uma função que conte de 100 até 1
# Pedir ao usuário qual função deve usar e ao final, exibir os dados solicitados!

def contar_de_1_a_100():
    for i in range(1, 101):
        print(i, end=' ')

def contar_de_100_a_1():
    for i in range(100, 0, -1):
        print(i, end=' ')

def main():
    escolha = input("Digite '1' para contar de 1 até 100 ou '2' para contar de 100 até 1: ")
    
    if escolha == '1':
        print("Contando de 1 até 100:")
        contar_de_1_a_100()
    elif escolha == '2':
        print("Contando de 100 até 1:")
        contar_de_100_a_1()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
