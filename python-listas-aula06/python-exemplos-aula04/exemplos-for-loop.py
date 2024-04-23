
# Exemplo 01:

for i in range(10):
    print('O valor de i é atualmente ', i + 1)

# Exemplo 02:

for i in range(1, 6):
    print(i + 1)

# Exemplo 03:

for i in range(2, 8, 3):
    print('O valor de i é: ', i)

# Exemplo 04:

power = 1
for expo in range(5):
    print('2 elevado a', expo, 'é', power)
    power *= 2 # power = power * 2

# exemplificando o exemplo 04:
# 2^1 - 2^2 - 2^3 - 2^4 e 2^5
# 2, 4, 8, 16 e 32

# Exemplo 05:

import time
for second in range(1, 6):
    print(second, 'Contando')
    time.sleep(1)

print('Pronto ou não, lá vou eu!')