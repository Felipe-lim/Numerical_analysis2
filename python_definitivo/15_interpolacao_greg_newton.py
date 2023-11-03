class Dado:
    # Número de pontos
    m = 5
    # Valores de x
    x = [0.1, 0.3, 0.4, 0.6, 0.7]
    # Valores correspondentes de y
    y = [0.3162, 0.5477, 0.6325, 0.7746, 0.8367]
    # Ponto para estimativa
    z = 0.2

    # Resultado esperado da interpolação
    #resultado = 0.4456

"""
Este código implementa o método de interpolação de Gregory-Newton para estimar valores dentro de um conjunto de dados conhecidos.
Ele é particularmente útil quando se tem uma tabela de diferenças divididas e se deseja encontrar um valor intermediário (z).
A classe 'Dado' contém os dados necessários para a interpolação.
"""

def inter_greg_new(m, x, y, z):
    # Inicializa a tabela de diferenças divididas com os valores de y
    dely = list(y)

    # Construção da tabela de diferenças divididas
    for k in range(1, m):
        for i in range(m - 1, k - 1, -1):
            # Calcula diferença dividida de ordem k
            dely[i] = (dely[i] - dely[i - 1])

    # Inicializa r com o termo mais à direita da tabela (última diferença dividida)
    r = dely[m - 1]
    # Calcula o termo u da fórmula de interpolação
    u = (z - x[0]) / (x[1] - x[0])

    # Loop para calcular o valor interpolado r
    for i in range(m - 2, -1, -1):
        # Calcula o próximo termo da série de Gregory-Newton
        # Obs: A expressão original (i + dely[i]) parece estar incorreta, pois as diferenças divididas não devem ser somadas aos índices.
        r = r * (u - i + 1) / (i + dely[i])  # O comentário indica que esta linha pode conter um erro.

    # Exibe o resultado da interpolação
    print(r)

# Chama a função com os dados fornecidos
inter_greg_new(Dado.m, Dado.x, Dado.y, Dado.z)
