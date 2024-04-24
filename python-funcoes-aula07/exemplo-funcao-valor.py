
# Criando uma função
def introducao(primeiro_nome, ultimo_nome='Smith'):
    print('Olá, meu nome é: ', primeiro_nome, ultimo_nome)

# Chamando a função
introducao('James', 'Bond') # Chamamos a função, passando dois valores, James e Bond, então não será atribuido o valor pré-definido (Smith)
introducao('James') # Aqui chamaos a função sem o segundo valor, colocando apenas o primeiro_nome (James), então será atribuido automático o valor pré-definido (Smith)