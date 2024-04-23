
# etapa 1

banda = []
print('etapa 1:', banda)

# etapa 2

banda.append('John Lennon')
banda.append('Paul McCartney')
banda.append('George Harrison')
print('etapa 2:', banda)

# etapa 3

for members in range(2):
    banda.append(input('Novo membro: '))
print('etapa 3:', banda)

# etapa 4

del banda [-1]
del banda [-1]
print('etaá 4:', banda)

# etapa 5
banda.insert(0, 'RingoStarr')
print('etapa 5:', banda)
print('The Beatles:', len(banda))