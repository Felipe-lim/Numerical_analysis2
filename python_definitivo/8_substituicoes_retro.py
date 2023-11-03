class Dado:

   U =[[5, -2, 6,  1],
       [0,  3, 7, -4],
       [0,  0, 4,  5],
       [0,  0, 0,  2]]
            
   D = [1, -2, 28, 8]


"""
O código resolve um sistema de equações lineares representado 
por uma matriz triangular superior U e um vetor D, usando o método 
das substituições retroativas. Ele calcula e imprime o vetor solução 
do sistema.
"""

def substituicoes_retroativas(U, D):
    n = len(U) -1  # Determina o número de linhas da matriz U e subtrai 1
    x = [0] * (n + 1)  # Inicialize o vetor de solução x com zeros
    
    # Calcula a última solução, xn = Dn/Unn
    x[n] = round(D[n] / U[n][n])  
    
    # Loop que percorre da penúltima até a primeira linha da matriz
    for i in range(n-1, -1, -1):
        soma = 0  # Inicializa a variável soma

        # Loop que percorre todas as colunas da diagonal principal até a última coluna
        for j in range(n, i, -1):
            # Soma Uij * xj
            soma += U[i][j] * x[j]  
        
        # Calcula a solução atual xi
        x[i] = round((D[i] - soma) / U[i][i], 2)
        
    # Imprime o vetor de soluções x
    print("A solução do sistema é:", x)  

# Chamada da função usando a matriz U e vetor D da classe Dado
substituicoes_retroativas(Dado.U, Dado.D)
