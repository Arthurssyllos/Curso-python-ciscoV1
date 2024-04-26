# import math
# import sys

## ou

import math , sys # Importante as bibliotecas instaladas

print(math.sin(math.pi/2)) # Utilizando as funções da biblioteca math

# Quando eu quero usar apenas uma função específica da biblioteca:

from math import sin, pi # Importanto a biblioteca, e dela especificamente as funções sin e pi

print(sin(pi/2)) # Aqui não utilimos o math.sin como no exemplo acima pois já especificamos no import da biblioteca as funções que queríamos

from math import e, exp, log # Importando outras funções da biblioteca math

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

## Colocando 'Apelidos', o chamado 'alias', nas importações de bibliotecas:

import math as m  # Importando a biblioteca math com o apelido de 'm'

print(m.sin(m.pi/2)) # Como não importei as funções específicas da biblioteca math, uso o m.sin, m do apelido de 'math' e .sin para acessar a função específica de seno

from math import pi as PI, sin as seno # Aqui importei da biblioteca math as funções específicas, porém com apelidos

print(seno(PI/2))
