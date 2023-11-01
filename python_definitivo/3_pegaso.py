class Dado:
    a = 0.5  # Ponto inicial a do intervalo.
    b = 1.0  # Ponto final b do intervalo.
    eps = 10e-2  # Tolerância do erro.
    imax = 20  # Número máximo de iterações.

    # Função que queremos encontrar a raiz.
    def f(x):
        y = x**3 - 9*x + 5
        return y

def pegaso():
    # Inicializando variáveis com os valores do problema.
    a = Dado.a
    b = Dado.b
    tol = Dado.eps

    fa = Dado.f(a)  # Calculando f(a).
    fb = Dado.f(b)  # Calculando f(b).

    # Verificando se a função muda de sinal no intervalo [a, b].
    if fa * fb > 0:
        print("A função não muda de sinal nos extremos do intervalo")
        return 1

    x = b  # Inicializando x com o valor de b.
    fx = fb  # Inicializando fx com o valor de f(b).

    # Loop principal para as iterações do método.
    for i in range(Dado.imax):

        # Calculando o incremento em x usando a fórmula do método de Pégaso.
        delta_x = -fx / (fb - fa) * (b - a)
        x += delta_x  # Atualizando o valor de x.
        fx = Dado.f(x)  # Calculando f(x) para o novo valor de x.

        # Imprimindo os valores de cada iteração.
        print(i, a, fa, b, fb, x, fx, delta_x)

        # Verificando a condição de parada.
        if abs(delta_x) <= tol and abs(fx) <= tol:
            break

        # Atualizando os valores de a, fa, b e fb para a próxima iteração.
        if fx * fb < 0:
            a = b  # Atualizando o valor de a.
            fa = fb  # Atualizando o valor de f(a).
        else:
            # Atualizando o valor de f(a) se fx e fb possuem o mesmo sinal.
            fa = (fa * fb) / (fb + fx)

        b = x  # Atualizando o valor de b.
        fb = fx  # Atualizando o valor de f(b).

    # Verificando se a solução convergiu.
    if abs(delta_x) <= tol and abs(fx) <= tol:
        print(" A raiz foi encontrada!!!\n", x)  # Imprimindo a raiz encontrada.
        return 0  # Retornando 0 se a raiz foi encontrada.

    else:
        print("A raiz não foi encontrada.")  # Imprimindo uma mensagem se a raiz não foi encontrada.
        return 1  # Retornando 1 se a raiz não foi encontrada.

# Chamando a função pegaso.
pegaso()
