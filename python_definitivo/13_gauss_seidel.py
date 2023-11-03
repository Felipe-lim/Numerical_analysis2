class Dado:

    # Matriz de coeficientes
    A =[[ 10,  3,  -2],
        [ 2,   8,  -1],
        [ 1,   1,   5]]
            
    # Vetor de termos independentes
    B = [57,  20,  -4]

    # Tolerância do erro para o critério de parada
    eps = 10e-6
    # Número máximo de iterações
    imax = 50

import copy

"""
O código realiza a resolução de um sistema de equações lineares através do método de Gauss-Seidel. 
Ele itera sobre um conjunto de equações ajustando as estimativas de solução até que a mudança seja 
menor que a tolerância estabelecida ou atinja um máximo de iterações.
"""

# Implementação do método de Gauss-Seidel para resolução de sistemas de equações lineares
def gauss_jord(A, B, Tol, imax):

    # Cria cópias dos dados para não alterar os valores originais durante os cálculos
    a = copy.deepcopy(A)
    b = copy.deepcopy(B)
    x = []  # Lista para armazenar a solução
    n = len(a)  # Número de linhas da matriz A (também número de equações)

    # Pré-processamento: Normaliza a matriz A pela diagonal principal e atualiza o vetor B
    for i in range(n):
        r = 1/a[i][i]  # Fator de normalização para a linha i
        for j in range(n):
            if i != j:
                a[i][j] = a[i][j] * r  # Normaliza os elementos fora da diagonal
        b[i] = b[i] * r  # Atualiza o vetor B
        x.append(b[i])  # Inicializa a solução com os valores normalizados do vetor B
    
    # Processo iterativo do método de Gauss-Seidel
    for k in range(imax):
        v = []  # Lista para armazenar a solução do passo anterior
        for i in range(n):
            soma = 0  # Acumulador para a soma das multiplicações
            for j in range(n):
                if i != j:
                    soma = soma + a[i][j] * x[j]  # Soma os produtos dos coeficientes pelos valores atuais da solução

            v.append(x[i])  # Guarda o valor atual da solução
            x[i] = b[i] - soma  # Atualiza o valor da solução com o novo cálculo

        # Avaliação da convergência
        norma_num = 0  # Numerador da norma
        norma_den = 0  # Denominador da norma
        for i in range(n):
            t = abs(x[i] - v[i])  # Diferença absoluta entre os valores atual e anterior da solução

            if t > norma_num:
                norma_num = t  # Atualiza o numerador da norma
            
            if abs(x[i]) > norma_den:
                norma_den = abs(x[i])  # Atualiza o denominador da norma
        
        norma_rel = norma_num/norma_den  # Calcula a norma relativa
        print(k, x, norma_rel)  # Exibe o número da iteração, a solução atual e a norma relativa

        # Teste de convergência
        if norma_rel <= Tol:
            break  # Finaliza o processo iterativo se a convergência for alcançada
        
    # Determinação se a solução foi encontrada dentro da tolerância especificada
    if norma_rel <= Tol:
        cond_erro = 0  # Código de erro 0 indica sucesso
    else:
        cond_erro = 1  # Código de erro 1 indica que o método não convergiu dentro das iterações definidas
    
# Executa o método de Gauss-Seidel com os dados fornecidos
gauss_jord(Dado.A, Dado.B, Dado.eps, Dado.imax)
