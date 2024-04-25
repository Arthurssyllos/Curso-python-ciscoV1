# Criando uma dicionário com um sub-condicionário em que nas notas, contém uma lista
students = {

    'João': {
        'idade': 18,
        'cidade':'São Paulo',
        'notas': [7.5, 8.0, 9.0]
    },

    'Maria': {
        'idade':20,
        'cidade':'Rio de Janeiro',
        'notas': [6.5, 7.0, 8.5]
    },

    'Pedro': {
        'idade': 19,
        'cidade':'Belo Horizonte',
        'notas':[8.0, 8.5, 9.5]
    }

}

## Desafio -- Para o dicionário acima:
 # 1° Imprimir a idade de João
 # 2° Adicionar uma nota para Maria
 # 3° Exibir todos os itens cadastrados.

print("1° Imprimir a idade de João:")
print("Idade de João:", students['João']['idade'])

print("\n2° Adicionar uma nota para Maria:")
students['Maria']['notas'].append(9.0)
print("Notas de Maria:", students['Maria']['notas'])

print("\n3° Exibir todos os itens cadastrados:")
for nome, info in students.items():
    print("Nome:", nome)
    print("Idade:", info['idade'])
    print("Cidade:", info['cidade'])
    print("Notas:", info['notas'])
    print()