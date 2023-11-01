class Dado:

    A =[[ 1,  6,  2,   4],
        [ 3, 19,  4,  15],
        [ 1,  4,  8, -12],
        [ 5, 33,  9,   3]]
            
    B = [8, 25, 18, 72]

def print_matrix(matrix, mb):
    # Função para imprimir a matriz e o vetor lado a lado
    ind = 0
    for i in matrix:
        print(i, mb[ind])
        ind +=1
    print("\n")

import copy

def gauss_jord(A, B):
    # Criando cópias profundas de A e B para evitar modificar as listas originais
    a = copy.deepcopy(A)
    b = copy.deepcopy(B)

    # Inicializando o determinante e o tamanho da matriz
    det = 1
    n = len(a)

    print_matrix(a,b)  # Imprimindo a matriz inicial e o vetor B

    # Loop principal para o processo de Gauss-Jordan
    for k in range(n):

        pivot = a[k][k]  # Pivot atual

        # Verificando se a matriz é singular
        if (pivot == 0):
            print("Gauss: singular matrix")
            return 0

        # Normalizando a linha k pelo valor do pivot
        for j in range(n):
            a[k][j] /= pivot
        b[k] /= pivot

        # Atualizando o determinante
        det *= pivot

        # Zerando os outros elementos da coluna k
        for j in range(n):
            if j != k:
                t = a[j][k]  # Fator de escala para subtrair a linha k
                for i in range(n):
                    a[j][i] -= t * a[k][i]  # Subtraindo um múltiplo da linha k da linha j
                b[j] -= t * b[k]  # Atualizando o vetor b de forma similar

    print_matrix(a,b)  # Imprimindo a matriz resultante e o vetor b

# Chamando a função gauss_jord com as matrizes e vetores definidos
gauss_jord(Dado.A, Dado.B)
