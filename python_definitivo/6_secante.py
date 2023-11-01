class Dado:
    a = 0.5 # ponto a
    b = 1.0 # ponto b
    eps = 10e-2 # Tolerância do erro
    imax = 20 # número máximo de iterações

    # função problema
    def f(x):
        y = x**3-9*x+5
        return y

def secante():

    print("Se retornar 0, a raiz foi encontrada. Senão, retorna 1")

    # recebendo Dados do problema
    a = Dado.a 
    b = Dado.b 
    tol = Dado.eps

    # calculando f(a) e f(b)
    fa = Dado.f(a)
    fb = Dado.f(b)

    # se o valor absoluto de f(a) for maior que f(b), então eles devem trocar
    if(abs(fa) < abs(fb)):
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

        delta_x = -fx/(fb-fa)*(b-a) # Calcula o incremento para x
        x += delta_x 
        fx = Dado.f(x)

        # atualizando valores para a nova iteração
        x = b - (fb * (b-a))/(fb - fa)
        fx = Dado.f(x)

        # printando resultados
        print(i, a, fa, b, fb, x, fx, delta_x)

        # testando condição de parada
        if(abs(delta_x) <= tol and abs(fx) <= tol): # Condições de parada
            break
            
        # atualizando valores para a nova iteração
        a = b 
        fa = fb 
        b = x 
        fb = fx 

    raiz = x 

    # teste de convergência
    if(abs(delta_x) <= tol and abs(fx) <= tol): # Verifica se as condições de parada foram atendidas
        print(" A raiz foi encontrada!!!\n", raiz)
        return 0

    else:
        print("A raiz não foi encontrada.")
        return 1 

secante()
