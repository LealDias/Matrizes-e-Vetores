# Álgebra Linear: Vetores e Matrizes

## Índice

1. [Vetores](#vetores)
2. [Operações com Vetores](#operações-com-vetores)
3. [Matrizes](#matrizes)
4. [Operações com Matrizes](#operações-com-matrizes)
5. [Código em Python](#código-em-python)

## Vetores

Um vetor é uma entidade matemática que possui magnitude (tamanho) e direção. Em Álgebra Linear, os vetores são representados como sequências ordenadas de números. Por exemplo, um vetor bidimensional pode ser representado como:

\[ \mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \]

onde \( v_1 \) e \( v_2 \) são números reais que indicam as coordenadas do vetor no plano.

## Operações com Vetores

### Adição de Vetores

A adição de vetores é feita componente por componente. Por exemplo, se temos dois vetores:

\[ \mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \]
\[ \mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} \]

então a soma \( \mathbf{v} + \mathbf{w} \) é dada por:

\[ \mathbf{v} + \mathbf{w} = \begin{bmatrix} v_1 + w_1 \\ v_2 + w_2 \end{bmatrix} \]

### Multiplicação por Escalar

A multiplicação de um vetor por um escalar (número real) também é feita componente por componente. Por exemplo, se:

\[ \mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \]
\[ c \quad \text{é um escalar} \]

então \( c \mathbf{v} \) é dado por:

\[ c \mathbf{v} = \begin{bmatrix} c v_1 \\ c v_2 \end{bmatrix} \]

### Produto Escalar (Produto Interno)

O produto escalar entre dois vetores \( \mathbf{v} \) e \( \mathbf{w} \) é calculado como a soma dos produtos de suas componentes correspondentes. Se:

\[ \mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} \]
\[ \mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} \]

então o produto escalar \( \mathbf{v} \cdot \mathbf{w} \) é dado por:

\[ \mathbf{v} \cdot \mathbf{w} = v_1 w_1 + v_2 w_2 \]

## Matrizes

Uma matriz é uma tabela retangular de números (ou elementos), organizados em linhas e colunas. As matrizes são usadas para representar dados ou transformações lineares.

### Representação de Matrizes

Uma matriz \( A \) com \( m \) linhas e \( n \) colunas é representada como:

\[ A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} \]

onde \( a_{ij} \) representa o elemento na linha \( i \) e coluna \( j \) da matriz.

## Operações com Matrizes

### Adição de Matrizes

A adição de matrizes é feita elemento por elemento. Se tivermos duas matrizes \( A \) e \( B \) do mesmo tamanho, a soma \( A + B \) é dada por:

\[ A + B = \begin{bmatrix} a_{11} + b_{11} & a_{12} + b_{12} & \cdots & a_{1n} + b_{1n} \\ a_{21} + b_{21} & a_{22} + b_{22} & \cdots & a_{2n} + b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} + b_{m1} & a_{m2} + b_{m2} & \cdots & a_{mn} + b_{mn} \end{bmatrix} \]

### Multiplicação por Escalar

Multiplicar uma matriz por um escalar envolve multiplicar cada elemento da matriz pelo escalar.

### Multiplicação de Matrizes

A multiplicação de matrizes não é comutativa e é definida apenas quando o número de colunas da primeira matriz é igual ao número de linhas da segunda matriz. Se \( A \) é uma matriz \( m \times n \) e \( B \) é uma matriz \( n \times p \), então o produto \( AB \) é uma matriz \( m \times p \) onde cada elemento \( c_{ij} \) é dado por:

\[ c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj} \]

### Exemplo

Considere as seguintes matrizes:

\[ A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \]
\[ B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} \]

- **Adição de Matrizes:** 

\[ A + B = \begin{bmatrix} 1+5 & 2+6 \\ 3+7 & 4+8 \end{bmatrix} = \begin{bmatrix} 6 & 8 \\ 10 & 12 \end{bmatrix} \]

- **Multiplicação por Escalar:** 

Se \( c = 2 \), então:

\[ cA = \begin{bmatrix} 2 \cdot 1 & 2 \cdot 2 \\ 2 \cdot 3 & 2 \cdot 4 \end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 6 & 8 \end{bmatrix} \]

- **Multiplicação de Matrizes:** 

\[ AB = \begin{bmatrix} 1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\ 3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix} \]

## Código em Python

Aqui está o código em Python para realizar essas operações, usando a biblioteca `numpy`.

```python
import numpy as np

# Definindo os vetores
v = np.array([1, 2])
w = np.array([3, 4])

# Adição de vetores
soma_vetores = v + w
print(f'Soma dos vetores: {soma_vetores}')

# Multiplicação por escalar
c = 2
multiplicacao_por_escalar = c * v
print(f'Multiplicação do vetor {v} por escalar {c}: {multiplicacao_por_escalar}')

# Produto escalar (produto interno)
produto_escalar = np.dot(v, w)
print(f'Produto escalar dos vetores {v} e {w}: {produto_escalar}')

# Definindo as matrizes
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Adição de matrizes
soma_matrizes = A + B
print(f'Soma das matrizes:\n{soma_matrizes}')

# Multiplicação de matriz por escalar
multiplicacao_matriz_escalar = c * A
print(f'Multiplicação da matriz\n{A}\npor escalar {c}:\n{multiplicacao_matriz_escalar}')

# Multiplicação de matrizes
produto_matrizes = np.dot(A, B)
print(f'Produto das matrizes:\n{produto_matrizes}')
