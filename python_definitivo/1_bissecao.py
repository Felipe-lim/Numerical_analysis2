import math  # Importando o módulo math, mas ele não é usado no código.

# Classe contendo atributos relacionados ao problema.
class Dado:
    a = 0.5  # Ponto inicial do intervalo.
    b = 1.0  # Ponto final do intervalo.
    eps = 10e-3  # Tolerância, erro aceitável.
    imax = 20  # Número máximo de iterações permitidas.

    # Função que define o problema.
    @staticmethod  # Decorador de método estático, pois este método não depende da instância da classe.
    def f(x):
        y = x**3 - 9*x + 5  # Definição da função.
        return y


"""
O código realiza o método da bisseção para encontrar a raiz de uma função matemática. Ele verifica se há uma mudança de sinal entre 
os pontos iniciais do intervalo e, se houver, realiza iterações, reduzindo o intervalo pela metade a cada passo até que a aproximação 
da raiz esteja dentro da tolerância de erro especificada.
"""

# Função que implementa o método da bisseção.
def biss():

    print("Se retornar 0, a raiz foi encontrada. Senao, retorna 1")

    # Obtendo dados da classe Dado.
    tol = Dado.eps
    a = Dado.a
    b = Dado.b

    # Calculando os valores da função nos pontos extremos.
    fa = Dado.f(a)
    fb = Dado.f(b)

    # Verificando se a função muda de sinal no intervalo.
    if(fa * fb > 0):
        print("A função não muda de sinal nos extremos do intervalo")  
        return 1

    delta_x = abs(Dado.a - Dado.b)  # Calculando o comprimento inicial do intervalo.

    # Realizando as iterações.
    for i in range(Dado.imax):

        x = (a+b)/2  # Calculando o valor médio entre a e b.
        fx = Dado.f(x)  # Calculando o valor da função no ponto médio.

        # Imprimindo os resultados.
        print(i, a, fa, b, fb, x, fx, delta_x)

        # Testando a condição de parada.
        if (delta_x <= tol and abs(fx) <= tol):
            break

        # Atribuindo novo valor ao intervalo.
        if (fa*fx > 0):
            a = x
            fa = fx
        else:
            b = x
            fb = fx  
        
        delta_x = delta_x / 2  # Atualizando o valor de delta_x.

    # Definindo a raiz encontrada.
    raiz = x

    # Teste de convergência.
    if(delta_x <= tol and abs(fx) <= tol):
        print(" A raiz foi encontrada!!\n", raiz)  
        return 0
    else:
        print("A raiz não foi encontrada.")  
        return 1    

# Chamando a função biss().
biss()
