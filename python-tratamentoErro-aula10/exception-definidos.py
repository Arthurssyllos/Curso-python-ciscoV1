
# Existem algumas respostas para erros já definidas

## Segue o exemplo abaixo:

try:
    value = int(input('Entre com um número: '))
    print('O valor: ', value, 'dividido por um é: ', 1 / value)
except ValueError:
    print('Erro. Verifique o valor fornecido!')
except ZeroDivisionError:
    print('Não é possível fazer uma divisão por zero!!')

