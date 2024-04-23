usuario_palavra = input('Entre com uma palavra: ')
usuario_palavra = usuario_palavra.upper()
for letra in usuario_palavra:
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        print(letra)

# Agora quero que imprima as letras na mesma linha, solução 01:

usuario_palavra = input('Entre com uma palavra: ')
usuario_palavra = usuario_palavra.upper()
for letra in usuario_palavra:
    if letra in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        print(letra, end='') 

# Solução para o problema 02:

palavras_sem_vogais = ""
usuario_palavra = input('Entre com uma palavra: ')
usuario_palavra = usuario_palavra.upper()
for letra in usuario_palavra:
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        palavras_sem_vogais += letra
print(palavras_sem_vogais)