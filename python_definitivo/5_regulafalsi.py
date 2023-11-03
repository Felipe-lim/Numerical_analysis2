class Dado:
    a = 0.5 # ponto a
    b = 1.0 # ponto b
    eps = 10e-2 # Tolerancia do erro
    imax = 20 # numero max de iteracoes

    # função problema
    def f(x):
        y  = x**3-9*x+5
        return y

"""
O código executa o método da falsa posição (regula falsi) para encontrar uma raiz de uma função. 
Ele verifica se existe uma mudança de sinal entre dois pontos, ajusta intervalos e calcula novos 
pontos iterativamente até atender a tolerância de erro ou exceder o limite de iterações.
"""

def regulafalsi():

    print("Se retornar 0, a raiz foi encontrada. Senao, retorna 1")

    # recebendo Dados do problema
    a = Dado.a 
    b = Dado.b 
    tol = Dado.eps

    # calculando f(a) e f(b)
    fa = Dado.f(a)
    fb = Dado.f(b)

    # conferindo se os sinais são opostos em f de a e b
    if(fa*fb > 0):
        print("A função não muda de sinal nos extremos do intervalo")
        return 1

    # se o valor absoluto de f(a) for maior que f(b), então eles devem trocar
    if(fa > 0):
        t = a 
        a = b 
        b = t 
        
        t = fa 
        fa = fb 
        fb = t 

    x = b 
    fx = fb 

    # iteração principal
    for i in range(Dado.imax):

        delta_x = -fx/(fb-fa)*(b-a)
        x += delta_x 
        fx = Dado.f(x)

        # printando resultados
        print(i, a, fa, b, fb, x, fx, delta_x)

        # testando condição de parada
        if(abs(delta_x)  <= tol and abs(fx) <= tol):
            break
            
        # atualizando valores para a nova iteração
        if(fx < 0):
            a = x 
            fa = fx 
        else:
            b = x 
            fb = fx 

    raiz = x 

    # teste de convergência
    if(abs(delta_x) <= tol and abs(fx)<= tol):
        print(" A raiz foi encontrada!!!\n", raiz)
        return 0

    else:
        print("A raiz não foi encontrada.")
        return 1 

regulafalsi()
