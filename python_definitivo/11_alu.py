import numpy as np
import copy

"""
Este código executa a decomposição LU de uma matriz, que separa a matriz em componentes 
triangulares inferiores (L) e superiores (U). Ele é útil para resolver sistemas de equações 
lineares e calcular determinantes e inversas de forma eficiente.
"""

# Definição da classe Dado que possui as matrizes A e B como atributos de classe.
class Dado:

    # Matriz A será usada para o cálculo da decomposição LU.
    A =[[ 1,  6,  2,   4],
        [ 3, 19,  4,  15],
        [ 1,  4,  8, -12],
        [ 5, 33,  9,   3]]
            
    # Vetor B que seria o lado direito de um sistema Ax=B.
    B = [8, 25, 18, 72]

    # solucao = [-138, 20, 11, 1] # Comentário sobre a solução esperada (não utilizado no código).

# Função para imprimir matrizes.
def print_matrix(matrix):
    for i in matrix:
        print(i,)
    print("\n")

# Função para realizar a decomposição LU da matriz.
def lu(mA, mode = "separado"):
    """
    Computa a Fatoração LU com pivoteamento parcial de uma matriz (nxn)
    :param mA: Matriz Real e Quadrada
    :param mode: Especifica o formato de retorno dos dados (condensado ou separado)
        "separado": retorna Pivot, L, U, Det
        "condensado": retorna Pivot, LU, Det
    """
    
    # Imprime ação que está sendo realizada.
    print("Fazendo a decomposica LU")

    # Informa o que será retornado conforme o modo escolhido.
    if mode == "separado": 
        print("\t Retorna: P L U Det, com LU separada em uma matriz L e outra U")
    elif mode == "condensado": 
        print("\t Retorna P LU Det, com LU condensada em uma unica matriz")
    else: 
        raise Exception("Modo especificado incorretamente")

    # Cópia profunda da matriz para não alterar a original.
    A = copy.deepcopy(mA)
    n = len(A)

    # Inicialização do vetor de pivotamento.
    pivot = np.zeros(n, int)
    for i in range(n):
        pivot[i] = i

    # Determinante inicializado como 1.
    det = np.int64(1)

    # Laço para a decomposição LU com pivoteamento parcial.
    for j in range(0, n-1):
        # Escolha do elemento pivot.
        p = j
        amax = abs(A[j][j])
        for k in range(j+1, n):
            if abs(A[k][j]) > amax:
                amax = abs(A[k][j])
                p = k

        # Troca de linhas, se necessário.
        if p != j: 
            for k in range(0, n): # Troca de linhas
                A[j][k], A[p][k] = A[p][k], A[j][k]
            # Troca no vetor de pivotamento.
            pivot[j], pivot[p] = pivot[p], pivot[j]
            det *= -1  # Ajuste do determinante por troca de linhas.

        # Multiplicador do determinante.
        det *= A[j][j]

        # Eliminação de Gauss para zerar elementos abaixo do pivot.
        if abs(A[j][j]) != 0:
            r =1.0 / A[j][j]
            for i in range(j+1, n):
                mult = A[i][j] * r 
                A[i][j] = mult
                for k in range(j+1, n):
                    A[i][k] -= mult * A[j][k]

    # Atualização final do determinante.
    det *= A[n-1][n-1]

    # Retorno dos resultados de acordo com o modo.
    if mode == "separado":
        L = np.identity(n)  # Cria a matriz L (triangular inferior) como identidade.
        U = np.zeros((n,n))  # Cria a matriz U (triangular superior) como zeros.
        for i in range(n):
            U[i][i] = A[i][i]  # Copia a diagonal para U.
            for j in range(i):
                L[i][j] = A[i][j]  # Elementos abaixo da diagonal vão para L.
                U[j][i] = A[j][i]  # Elementos acima da diagonal vão para U.
        print(pivot, '\n\n', L, '\n\n', U, '\n\n', det)   

    elif mode == "condensado":
        print( pivot, '\n\n', A, '\n\n', det)  # Retorna a matriz condensada e o determinante.

# Chamada da função lu com a matriz da classe Dado e modo "separado".
lu(Dado.A, "separado")
