tentativas = 0
while tentativas < 3:
    senha = input('Digite a senha: ')
    if senha == 'senha123':
        print('Acesso permitido!')
        break
    else:
        print('Senha, incorreta! Tente novamente.. Você tem apenas 3 tentativas e já foram feitas: ', tentativas +1)
        tentativas += 1
else:
    print('Você excedeu o número máximo de tentativas!')