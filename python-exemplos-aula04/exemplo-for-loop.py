
# exemplo 01 de loop

for i in range(6,1, -2):
    print(i, end =" ") # Saída: 6, 4, 2
print('\nfim exemplo 01!')

# exemplo 02 de loop

print('Inicío exemplo 02')
tipo = input("Digite.. 'par' ou 'impar': ")
for i in range(1, 11):
    if tipo == "par" and i % 2 == 0:
        print(i)
    elif tipo == "impar" and i % 2 !=0:
        print(i)
print('Fim exemplo 02!')

# exemplo 03 de loop

for i in range(1, 110):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'é divisível por 3 e 5')
    elif i % 3 == 0:
        print(i, 'por 3')
    elif i % 5 == 0:
        print(i, 'por 5')
    else:
        print(i)