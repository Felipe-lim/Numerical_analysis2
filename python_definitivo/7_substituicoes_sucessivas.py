class Dado:
    # Matriz triangular inferior L e vetor C (termos constantes)
    L =[[ 2,  0,  0, 0],
        [ 3,  5,  0, 0],
        [ 1, -6,  8, 0],
        [-1,  4, -3, 9]]
            
    C = [4, 1, 48, 6]

"""
O código executa substituições sucessivas para resolver sistemas lineares 
com uma matriz triangular inferior (L). A função calcula e imprime o vetor 
solução (x), processando uma linha por vez e subtraindo os produtos conhecidos 
das soluções anteriores.
"""

def substituicoes_sucessivas(L, C):

    n = len(L)  # Determina o número de linhas da matriz L
    x = [0] * n  # Inicialize o vetor de solução x com zeros
    
    x[0] = C[0] / L[0][0]  # Calcula a primeira solução, x1 = C1/L11
    
    # Loop que percorre de segunda até a última linha da matriz
    for i in range(1, n):
        soma = 0  # Inicializa a variável soma

        # Loop que percorre todas as colunas até a diagonal principal
        for j in range(i):
            soma += L[i][j] * x[j]  # Soma Lij * xj
        
        # Calcula a solução atual xi
        x[i] = (C[i] - soma) / L[i][i]

    print("A solução do sistema é:", x)  # Retorna o vetor de soluções x

# Chamada da função usando a matriz L e vetor C da classe Dado
substituicoes_sucessivas(Dado.L, Dado.C)
