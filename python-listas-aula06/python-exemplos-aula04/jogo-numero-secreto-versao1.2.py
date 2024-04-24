from random import randint

numero_secreto = randint(1,100)
tentativa = 1 

while tentativa <= 3:
    palpite = int(input('Adivinhe o número secreto: '))
    if palpite == numero_secreto:
        print('Parabéns, você acertou!')
        break
    else:
        if palpite > numero_secreto:
            print('O número secreto é menor do que', palpite)
        else:
            print('O número secreto é maior do que', palpite)
    tentativa += 1

if tentativa > 3:
    print('Suas tentativas acabaram, o número secreto era', numero_secreto)


## jogo secreto versão 1.2