class Dado:

    # Matriz de coeficientes
    A = [[ 10,  3,  -2],
         [ 2,   8,  -1],
         [ 1,   1,   5]]

    # Vetor de termos independentes
    B = [57,  20,  -4]

    # Fator de sobre-relaxação
    Omega = 1.5

    # Tolerância para o critério de parada
    eps = 10e-2
    # Número máximo de iterações
    imax = 50

import copy

"""
Este código implementa o método Successive Over-Relaxation (SOR) para resolver sistemas lineares de equações. 
Utiliza iterações para melhorar sucessivamente uma estimativa da solução até que a mudança relativa entre as 
iterações seja menor que uma tolerância definida.

"""

# Implementação do método SOR
def sor(A, B, Omega, Tol, imax):

    # Cria cópias dos dados para evitar a modificação dos dados originais
    a = copy.deepcopy(A)
    b = copy.deepcopy(B)
    x = []  # Inicializa a lista que armazenará a solução
    n = len(a)  # Tamanho da matriz A (quantidade de equações)

    # Normalização da matriz A e vetor B
    for i in range(n):
        r = 1/a[i][i]  # Fator para normalizar a linha i
        for j in range(n):
            if i != j:
                a[i][j] *= r  # Normaliza os elementos fora da diagonal principal

        b[i] *= r  # Normaliza os termos independentes
        x.append(b[i])  # Usa os termos independentes normalizados como chute inicial
    
    # Iterações do método SOR
    for k in range(imax):
        v = []  # Armazena a solução do passo anterior
        for i in range(n):
            soma = 0  # Soma dos aij * xj
            for j in range(n):
                if i != j:
                    soma += a[i][j] * x[j]  # Acumula o somatório
            
            v.append(x[i])  # Guarda o valor atual de xi
            # Atualiza xi usando a fórmula de sobre-relaxação
            x[i] = Omega * (b[i] - soma) + (1 - Omega) * x[i]

        norma_num = 0  # Numerador da norma
        norma_den = 0  # Denominador da norma
        # Calcula as normas para o critério de parada
        for i in range(n):
            t = abs(x[i] - v[i])  # Diferença absoluta entre as soluções atual e anterior
            
            if t > norma_num:
                norma_num = t  # Atualiza o maior numerador encontrado

            if abs(x[i]) > norma_den:
                norma_den = abs(x[i])  # Atualiza o maior denominador encontrado
        
        norma_rel = norma_num / norma_den  # Calcula a norma relativa

        print(k, x, norma_rel)  # Exibe o número da iteração, a solução e a norma relativa

        # Teste de convergência
        if norma_rel <= Tol:
            break  # Se atende ao critério de parada, interrompe as iterações

    # Verifica se a solução foi encontrada dentro da tolerância especificada
    if norma_rel <= Tol:
        cond_erro = 0  # Indica sucesso
    else:
        cond_erro = 1  # Indica falha ao não convergir dentro do número máximo de iterações

# Executa o método SOR com os dados da classe Dado
sor(Dado.A, Dado.B, Dado.Omega, Dado.eps, Dado.imax)
