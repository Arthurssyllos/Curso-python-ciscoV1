
# Problema: Se você entrar com um número igual a zero, ele irá dar erro

value = int(input('Entre com um número: '))

print('O valor: ', value, 'dividido por um é: ', 1/value)

# A solução para o problema é usar o tratamento de erro, que se o usuário tentar, irá aparecer uma mensagem ou algo relacionado sobre o erro específico:

## Usar o try-except

### try:

    # local do código

### except:

    # local para o tratamento de erros

## Exemplo:

try:
    value = int(input('Entre com um número: '))
    print('O valor: ', value, 'um dividido por valor é: ', 1/value)        
except:
    print('Erro. Verifique o valor fornecido.')
