class Dado:
    m = 5  # Define o número de pontos dados
    x = [0.1, 0.3, 0.4, 0.6, 0.7]  # Pontos no eixo x para interpolação
    y = [0.3162, 0.5477, 0.6325, 0.7746, 0.8367]  # Pontos no eixo y correspondentes
    z = 0.2  # O ponto x para o qual se deseja encontrar o valor de y interpolado

    #resultado esperado da interpolação

"""
Este código implementa o método de interpolação polinomial de Newton.
Ele calcula um valor estimado para um dado ponto 'z' utilizando os pontos conhecidos 'x' e 'y'.
A classe 'Dado' armazena os valores dos pontos e o ponto 'z' para o qual a interpolação é desejada.
"""

def inter_newton(m, x, y, z):
    # Copia os valores de y para dely para inicializar a tabela de diferenças divididas
    dely = list(y)  

    # Calcula a tabela de diferenças divididas
    for k in range(1, m):
        for i in range(m - 1, k - 1, -1):
            # Atualiza dely[i] com a diferença dividida de ordem k
            dely[i] = (dely[i] - dely[i - 1]) / (x[i] - x[i - k])

    # Inicializa o valor interpolado r com o termo de ordem mais alta da tabela
    r = dely[m - 1]  # Use m - 1 pois os índices em Python começam em 0

    # Calcula o valor interpolado para z usando a tabela de diferenças divididas
    for i in range(m - 2, -1, -1):
        # Combina os termos do polinômio de Newton de trás para frente
        r = r * (z - x[i]) + dely[i]

    # Imprime o resultado da interpolação
    print(r)

# Executa a função de interpolação com os dados fornecidos
inter_newton(Dado.m, Dado.x, Dado.y, Dado.z)
