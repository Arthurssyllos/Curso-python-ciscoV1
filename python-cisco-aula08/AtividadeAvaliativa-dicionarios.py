## Exercícios Dicionários!

# 1° Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.

# 2° Escreva uma função que receba Nome e Idade. Retorne valores que contêm a chave "idade" e cujo valor é maior que 18.

# 3° Escreva uma função que receba duas listas de mesmo comprimento, uma contendo chaves e outra contendo valores, e retorna um dicionário criado a partir dessas listas.

# 4° Escreva uma função que receba um dicionário como entrada e retorna duas listas. Uma com chave e outra com valor.

# 5° Escreva uma função que receba um dicionário como entrada e retorna uma nova lista contendo apenas as chaves

# 6° Escreva uma função que receba um dicionário como entrada e retorna uma nova lista com as chaves ordenadas em ordem alfabética.


# Resolução do 1°:

def maior_chave_valor(dicionario):
  """
  Função que recebe um dicionário como entrada e retorna a chave com o maior valor.

  Argumento:
    dicionario: O dicionário a ser analisado.

  Retorno:
    A chave com o maior valor do dicionário.
  """
  chave_maior = max(dicionario, key=dicionario.get)
  return chave_maior

# Exemplo de uso
dicionario = {"a": 10, "b": 20, "c": 30}
chave_maior = maior_chave_valor(dicionario)
print(f"A chave com o maior valor é: {chave_maior}")  # Imprime: A chave com o maior valor é: c

# Resolução do 2°:

def filtrar_maiores_18(dicionario):
  """
  Função que recebe um dicionário como entrada e retorna um novo dicionário contendo apenas os itens com idade maior que 18.

  Argumento:
    dicionario: O dicionário a ser filtrado.

  Retorno:
    Um novo dicionário contendo apenas os itens com idade maior que 18.
  """
  maiores_18 = {nome: dados for nome, dados in dicionario.items() if dados["idade"] > 18}
  return maiores_18

# Exemplo de uso
dicionario = {"João": {"idade": 25}, "Maria": {"idade": 17}, "Pedro": {"idade": 32}}
maiores_18 = filtrar_maiores_18(dicionario)
print(f"Dicionário filtrado por maiores de 18 anos: {maiores_18}")  # Imprime: Dicionário filtrado por maiores de 18 anos: {'João': {'idade': 25}, 'Pedro': {'idade': 32}}

# Resolução do 3°:

def criar_dicionario(chaves, valores):
  """
  Função que recebe duas listas de mesmo comprimento, uma contendo chaves e outra contendo valores, e retorna um dicionário criado a partir dessas listas.

  Argumentos:
    chaves: A lista de chaves do dicionário.
    valores: A lista de valores do dicionário.

  Retorno:
    Um dicionário criado a partir das listas de chaves e valores.
  """
  if len(chaves) != len(valores):
    raise ValueError("As listas de chaves e valores devem ter o mesmo comprimento.")
  dicionario = dict(zip(chaves, valores))
  return dicionario

# Exemplo de uso
chaves = ["nome", "idade", "cidade"]
valores = ["João", 32, "São Paulo"]
dicionario = criar_dicionario(chaves, valores)
print(f"Dicionário criado a partir das listas: {dicionario}")  # Imprime: Dicionário criado a partir das listas: {'nome': 'João', 'idade': 32, 'cidade': 'São Paulo'}

# Resolução do 4°:

def separar_chaves_valores(dicionario):
  """
  Função que recebe um dicionário como entrada e retorna duas listas: uma com as chaves e outra com os valores.

  Argumento:
    dicionario: O dicionário a ser separado.

  Retorno:
    Duas listas: uma com as chaves e outra com os valores do dicionário.
  """
  chaves = list(dicionario.keys())
  valores = list(dicionario.values())
  return chaves, valores

# Exemplo de uso
dicionario = {"a": 1, "b": 2, "c": 3}
chaves, valores = separar_chaves_valores(dicionario)
print(f"Lista de chaves: {chaves}")  # Imprime: Lista de chaves: ['a', 'b', 'c']
print(f"Lista de valores: {valores}")  # Imprime: Lista de valores: [1, 2, 3]

# Resolução do 5°:

def obter_chaves(dicionario):
  """
  Função que recebe um dicionário como entrada e retorna uma nova lista contendo apenas as chaves do dicionário.

  Argumento:
    dicionario: O dicionário a ser utilizado.

  Retorno:
    Uma nova lista contendo apenas as chaves do dicionário.
  """
  chaves = list(dicionario.keys())
  return chaves

# Exemplo de uso
dicionario = {"a": 1, "b": 2, "c": 3}
lista_chaves = obter_chaves(dicionario)
print(f"Lista de chaves: {lista_chaves}")  # Imprime: Lista de chaves: ['a', 'b', 'c']

# Resolução do 6°:

def ordenar_chaves_alfabeticamente(dicionario):
  """
  Função que recebe um dicionário como entrada e retorna uma nova lista contendo as chaves ordenadas em ordem alfabética.

  Argumento:
    dicionario: O dicionário a ser ordenado.

  Retorno:
    Uma nova lista contendo as chaves do dicionário ordenadas em ordem alfabética.
  """
  chaves_ordenadas = sorted(dicionario.keys())
  return chaves_ordenadas

# Exemplo de uso
dicionario = {"c": 3, "a": 1, "b": 2}
lista_chaves_ordenadas = ordenar_chaves_alfabeticamente(dicionario)
print(f"Lista de chaves ordenadas alfabeticamente: {lista_chaves_ordenadas}")  # Imprime: Lista de chaves ordenadas alfabeticamente: ['a', 'b', 'c']
