class Dado:
    x_start = 0.5  # Ponto inicial para iniciar a busca pela raiz.
    eps = 10e-3  # Tolerância do erro, critério de parada.
    imax = 20  # Número máximo de iterações permitidas.

    def g(x):
        # Definição da função que será usada para calcular o próximo p.
        # Isso é baseado na manipulação da função original para x = g(x).
        y = (x**3 + 5)/9
        return y

"""
O código implementa o método do ponto fixo para encontrar a raiz de uma função. 
Ele itera uma função manipulada g(x), partindo de um valor inicial, até que a solução 
convirja para um ponto fixo com tolerância definida ou o número máximo de iterações 
seja alcançado.
"""

def ponto_fixo():
    p0 = Dado.x_start  # Inicializando com o valor de partida.
    TOL = Dado.eps  # Tolerância que determinará a precisão da solução.

    # Loop que continuará até que o número máximo de iterações seja atingido.
    for k in range(1, Dado.imax):

        p = Dado.g(p0)  # Calcula o novo p usando a função g(x).

        # Verificando se a diferença entre os valores sucessivos de p é menor que a tolerância.
        # Ou se a diferença relativa entre p e p0 é menor que a tolerância.
        # Ou se o valor de p é menor que a tolerância.
        if abs(p - p0) < TOL or abs((p - p0)/p) < TOL or abs(p) < TOL:
            print("O resultado é: ", p)  # Imprime o valor de p onde a função converge.
            print(k)  # Imprime o número de iterações que foram necessárias para convergir.
            return p  # Retorna o valor de p onde a função converge.

        p0 = p  # Atualiza p0 para a próxima iteração.

    # Se o método não convergiu dentro do número máximo de iterações, uma mensagem de erro é impressa.
    print("O método falhou depois de %n iterações", Dado.imax)

# Chamando a função ponto_fixo para encontrar a raiz da função.
ponto_fixo()
