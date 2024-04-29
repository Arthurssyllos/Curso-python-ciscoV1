
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def escreveNome(exibir):
        print('Olá, meu nome é: ' + exibir.nome)
        print('Minha idade é: ', exibir.idade)

nome1 = Pessoa('Julia', 19)
nome1.escreveNome()

# Modificar o objeto

nome1.idade = 23
print(nome1.idade)

nome1.nome = 'Julinha'
print(nome1.nome)

# Apagar o objeto

del nome1.age
print(nome1.age)