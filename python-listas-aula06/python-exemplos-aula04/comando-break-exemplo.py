# break example

print('Comando Break:')
for i in range(1, 6):
    if i == 3:
        break
    print('Dentro do loop..', i)
print('Fora do loop...')

# Continue - Example

print('\nComando continue:')
for i in range(1, 6):
    if i ==3:
        continue
    print('Dentro do loop..', i)
print('Fora do loop...')