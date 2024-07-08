import numpy as np

# Definindo os vetores
v = np.array([1, 2])
w = np.array([3, 4])

# Adição de Vetores
soma_vetorial = v + w
print(f'Soma dos Vetores: {soma_vetorial}')

# Multiplicação por Escalar (c)
c = 2
multiplicacao_por_escalar = c * v
print(f'Multiplicação do Vetor {v} pelo escalar {c} é: {multiplicacao_por_escalar}')

# Produto Escalar (Produto Interno)
produtor_escalar = np.dot(v, w)
print(f'Produto escalar dos vetores {v} e {w}: {produtor_escalar}')

#Definição de Matrizes

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

print(A)
print(B)

# Soma das Matrizes
soma_matriz = A + B
print(f'Soma das Matrizes: \n{soma_matriz}')

# Multiplicação de Matriz por Escalar
multiplicacao_matriz_escalar = c * A
print(f'Multiplicação da matriz\n{A}\npor escalar {c}:\n{multiplicacao_matriz_escalar}')

# Multiplicação de matrizes
produto_matrizes = np.dot(A, B)
print(f'Produto das matrizes:\n{produto_matrizes}')