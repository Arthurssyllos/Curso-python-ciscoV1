while True:
    try:
        numero = int(input('Entre com número: '))
        print (5/numero)
        break
    except (ValueError, ZeroDivisionError):
        print('Valor errado ou não é possível dividir por zero..')
    except:
        print('Desculpe, algo errado aconteceu : (')