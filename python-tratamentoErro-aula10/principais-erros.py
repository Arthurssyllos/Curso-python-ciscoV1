
## Principais erros !

# ZeroDivisionError   
# ValueError                    
# TypeError
# AttributeError
# SyntaxError

### ZeroDivisionError
### Esta exceção é levantada quando há uma tentativa de divisão por zero em Python.
### Por exemplo, se você tentar executar a seguinte operação: 5 / 0, o Python levantará a exceção ZeroDivisionError.

# Exemplo de ZeroDivisionError
a = 10
b = 0
c = a/b
print(c)

### ValueError
### Esta exceção é levantada quando um argumento de uma função tem o tipo correto, mas um valor inválido. 
### Por exemplo, se você tentar converter uma string que não pode ser interpretada como um número em um inteiro usando a função int(), o Python levantará a exceção ValueError.

# Exemplo de ValueError
a = "abc"
b = int(a)
print(b)

### TypeError
### Esta exceção é levantada quando há uma operação ou função sendo aplicada a um objeto de um tipo incompatível. 
### Por exemplo, se você tentar somar uma string e um número, o Python levantará a exceção TypeError.

# Exemplo de TypeError
a = "abc"
b = 5
c = a + b
print(c)

### AttributeError
### Esta exceção é levantada quando um objeto não tem o atributo ou método que está sendo acessado.
### Por exemplo, se você tentar acessar o atributo length em um objeto que não possui esse atributo, o Python levantará a exceção AttributeError.

# Exemplo de AttributeError
a = "abc"
b = a.length
print(b)

# Exemplo corrigido de # AttributeError
a = "abc"
b = len(a)
print(b)

# str em Python não possui um 
# atributo length.

### SyntaxError
### Esta exceção é levantada quando há um erro de sintaxe no seu código Python. Por exemplo, se você tentar executar o seguinte código: if x = 5:, 
### o Python levantará a exceção SyntaxError, porque você está tentando atribuir um valor a uma variável dentro de uma declaração if, em vez de fazer uma comparação usando ==.

# Exemplo de SyntaxError
x = 5
if x = 5:
    print("x é igual a 5")

# forma correta
x = 5
if x == 5:
    print("x é igual a 5")