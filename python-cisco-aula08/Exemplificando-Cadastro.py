# Criando um dicionário vazio (sem nada)
cadastro = {}

while True: # Entrou no loop (pois já colocamos como True)
    nome = input('Digite o nome completo: ')
    if nome == '':
        break # Se o usuário não digitar nada em branco, irá continuar o loop do if

    idade = int(input('Digite a sua idade: '))
    cidade = input('Digite a cidade: ')

    # Adiciona os dados ao dicionário
    cadastro[nome] = {
        'idade': idade,
        'cidade': cidade # Nesse caso, cadastro é o nosso dicionário vazio, o [nome] é a chave, e atribuimos com o sinal de =, uma outro dicionario dentro de cadastro
    }

# Imprime o cadastro completo
print('Cadastro')
print(cadastro)
for nome, dados in cadastro.items(): # Aqui colocamos duas variáveis a qual, é nome (chave) e dados (valor), no dicionário cadastro, e o .items() é para acessar os dois itens.
    print('- Nome:', nome)
    print('- Idade:', dados['idade']) # Aqui atribuimos que para a variável dados é a idadade
    print('- Cidade:', dados['cidade'])