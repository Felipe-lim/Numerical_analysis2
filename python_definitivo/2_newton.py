class Dado:
    x0 = 0.5  # Definindo o valor inicial da aproximação da raiz.
    eps = 10e-2  # Definindo a tolerância do erro.
    imax = 20  # Definindo o número máximo de iterações.

    # Definindo a função cuja raiz queremos encontrar.
    def f(x):
        return x**3 - 9*x + 5

    # Calculando a derivada numérica da função.
    def df(x):
        h = 1e-5  # Definindo um pequeno valor de h para calcular a derivada.
        # Usando a fórmula de diferenças centradas para aproximar a derivada.
        df_x = (Dado.f(x + h) - Dado.f(x - h)) / (2 * h)
        return round(df_x, 5)  # Arredondando o valor da derivada.

"""
O código implementa o método de Newton-Raphson para encontrar uma aproximação de uma raiz de uma função, utilizando uma derivada 
numérica. Começando de um ponto inicial, o método itera melhorando a estimativa até que a solução satisfaça uma tolerância de erro 
ou até um número máximo de iterações.
"""

def newton():
    tol = Dado.eps  # Obtendo a tolerância do erro.
    x0 = Dado.x0  # Obtendo o valor inicial de x.

    fx = Dado.f(x0)  # Calculando o valor da função no ponto x0.
    dfx = Dado.df(x0)  # Calculando o valor da derivada no ponto x0.
    x = x0  # Atribuindo o valor inicial de x.

    # Imprimindo os valores iniciais.
    print(x, dfx, fx)

    for i in range(Dado.imax):  # Iterando até o número máximo de iterações.

        # Calculando o incremento de x usando a fórmula de Newton.
        delta_x = -fx / dfx
        x = x + delta_x  # Atualizando o valor de x.

        # Atualizando os valores de fx e dfx para o novo x.
        fx = Dado.f(x)
        dfx = Dado.df(x)

        # Imprimindo os valores calculados em cada iteração.
        print(i, x, dfx, fx, delta_x)

        # Checando as condições de parada: se o valor absoluto de delta_x ou fx é menor que a tolerância, ou se dfx é zero.
        if (abs(delta_x) <= tol and abs(fx) <= tol) or dfx == 0:
            break  # Parando o loop se qualquer condição de parada for atendida.

    # Testando se a solução convergiu.
    if abs(delta_x) <= tol and abs(fx) <= tol:
        print(" A raiz foi encontrada!!!\n", x)  # Imprimindo a raiz encontrada.
        return 0  # Retornando 0 se a raiz foi encontrada.
    else:
        print("A raiz não foi encontrada.")  # Imprimindo uma mensagem se a raiz não foi encontrada.
        return 1  # Retornando 1 se a raiz não foi encontrada.

# Chamando a função de Newton.
newton()

