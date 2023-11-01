class Dado:

    A =[[ 1,  6,  2,   4],
        [ 3, 19,  4,  15],
        [ 1,  4,  8, -12],
        [ 5, 33,  9,   3]]
            
    B = [8, 25, 18, 72]
    
    solucao = [-138, 20, 11, 1]

def substituicoes_retroativas(U, D):
    # Definindo o número de variáveis
    n = len(U) -1  
    x = [0] * (n + 1)  # Inicializa o vetor de solução com zeros
    
    # Calculando a última variável
    x[n] = round(D[n] / U[n][n], 2)  
    
    # Iterando sobre as linhas restantes para encontrar as outras variáveis
    for i in range(n-1, -1, -1):
        soma = 0
        # Calculando a soma dos produtos das variáveis já encontradas
        for j in range(n, i, -1):
            soma += U[i][j] * x[j]  
        
        # Calculando a variável atual
        x[i] = round((D[i] - soma) / U[i][i], 2)
    
    return x  # Retorna o vetor solução


def print_matrix(matrix, mb):
    ind = 0
    for i in matrix:
        print(i, mb[ind])
        ind +=1
    print("\n")


import copy

def gauss(A, B):
    # Criando cópias profundas das listas para evitar modificar as originais
    a = copy.deepcopy(A)
    b = copy.deepcopy(B)

    # Inicializando o determinante e o tamanho da matriz
    det = 1
    n = len(a)

    # Iteração principal para a eliminação de Gauss
    for k in range(n-1):
        
        # Procurando o maior pivo na coluna k
        maior_celula = 0
        for i in range(k, n):
            if (abs(maior_celula) < abs(a[i][k])):
                maior_celula = a[i][k]
                maior_linha = i

        # Verificando se a matriz é singular
        if (maior_celula == 0):
            print("Gauss: singular matrix")
            return 0

        # Trocando linhas para colocar o maior pivo na posição correta, se necessário
        if (maior_linha != k):
            a[maior_linha], a[k] = a[k], a[maior_linha]
            b[maior_linha], b[k] = b[k], b[maior_linha]

        # Atualizando o determinante
        det *= a[k][k]

        # Fazendo a matriz triangular superior
        for j in range(k+1, n):
            t = a[j][k] / a[k][k]
            for i in range(n):
                a[j][i] -= t * a[k][i]
            
            b[j] -= t * b[k]

    # Resolvendo o sistema triangular superior resultante
    solucao = substituicoes_retroativas(a, b)
    print_matrix(a, b) # Imprimindo a matriz triangular e o vetor modificado
    print("A solucao é", solucao) # Retornando o vetor de soluções

# Chamando a função gauss com as matrizes e vetores definidos
gauss(Dado.A, Dado.B)
