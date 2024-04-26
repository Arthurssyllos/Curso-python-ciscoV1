
# Existem algumas respostas para erros já definidas, e abaixo inserimos também para caso o usuário entre com um valor diferente de numeros!

## Agora segue o exemplo caso o usuário insira um valor em que não seja tabelado:

try:
    value = int(input('Entre com um número: '))
    print('O valor: ', value, 'dividido por um é: ', 1/value)        
except ValueError:
    print('Erro. Verifique o valor fornecido.')
except ZeroDivisionError:
    print('Não é possível fazer divisão por zero.')  
except:
    print('Algo errado aconteceu!')