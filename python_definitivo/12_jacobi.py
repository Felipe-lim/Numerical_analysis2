import copy

# Define uma classe que contém a matriz A, o vetor B e parâmetros para o método de Jacobi.
class Dado:

    A =[[ 10,  3,  -2],  # Matriz de coeficientes
        [ 2,   8,  -1],
        [ 1,   1,   5]]
            
    B = [57,  20,  -4]  # Vetor de termos independentes

    eps = 10e-2  # Tolerância do erro para o critério de parada
    imax = 50  # Número máximo de iterações

"""
Este código implementa o método de Jacobi para resolver sistemas de equações lineares. 
Ele itera para melhorar a estimativa da solução até que a diferença entre iterações 
sucessivas seja menor que uma tolerância definida ou até que o número máximo de iterações seja alcançado.
"""


# Método de Jacobi para resolução de sistemas de equações lineares
def jacobi(A, B, Tol, imax):

    # Cria cópias dos dados para não modificar os originais durante as iterações
    a = copy.deepcopy(A)
    b = copy.deepcopy(B)
    x = []  # Inicializa o vetor solução
    n = len(a)  # Número de linhas da matriz A

    # Normaliza a matriz A e o vetor B pela diagonal principal da matriz A
    for i in range(n):
        r = 1 / a[i][i]
        for j in range(n):
            if i != j:
                a[i][j] = a[i][j] * r
        b[i] = b[i] * r
        x.append(b[i])  # Insere o termo normalizado no vetor solução

    # Processo iterativo do método de Jacobi
    for k in range(imax):
        v = []  # Vetor para armazenar a nova aproximação da solução
        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j:
                    soma += a[i][j] * x[j]  # Soma ponderada dos elementos fora da diagonal
            v.append(b[i] - soma)  # Atualiza o vetor com a nova aproximação
        
        # Calcula as normas para avaliar a convergência
        norma_num = 0
        norma_den = 0
        for i in range(n):
            t = abs(v[i] - x[i])
            if t > norma_num:
                norma_num = t
            if abs(v[i]) > norma_den:
                norma_den = abs(v[i])
            x[i] = v[i]  # Atualiza o vetor solução com a nova aproximação
        
        norma_rel = norma_num / norma_den  # Calcula a norma relativa
        print(k, x, norma_rel)  # Exibe o número da iteração, a solução atual e a norma relativa

        # Teste de convergência
        if norma_rel <= Tol:
            break  # Interrompe as iterações se alcançar a tolerância desejada

    # Define o código de erro baseado na convergência ou não
    if norma_rel <= Tol:
        cond_erro = 0  # Convergiu dentro da tolerância
    else:
        cond_erro = 1  # Não convergiu dentro do número máximo de iterações

# Executa o método de Jacobi utilizando os dados da classe Dado
jacobi(Dado.A, Dado.B, Dado.eps, Dado.imax)
