import math

"""
Este código realiza a integração numérica de uma função utilizando a fórmula de Newton-Cotes.
A função de integração, 'integ_new_c', aceita limites de integração, uma função alvo e parâmetros
que definem a regra de Newton-Cotes a ser aplicada. A função retorna o valor da integral computada
e uma condição de erro que indica se houve algum problema com os parâmetros de entrada.


Parâmetros de Saída:
- Integral: Valor numérico resultante da integração.
- CondErro: Indicador de condição de erro, onde:
  - CondErro = 0: Não houve erro de consistência dos parâmetros fornecidos.
  - CondErro = 1: Ocorreu um erro devido ao número de subdivisões 'n' ser menor que 1 ou maior que 8.
  - CondErro = 2: Ocorreu um erro porque o resto da divisão de 'm' por 'n' não é zero, indicando uma distribuição inconsistente dos intervalos de integração.
  - CondErro = 3: Ambas as condições anteriores ocorreram, ou seja, 'n' está fora do intervalo permitido e o resto da divisão de 'm' por 'n' não é zero.

"""

class Dado:
    # Limites de integração
    a = 0
    b = math.pi  # Valor de Pi mais preciso usando 'math.pi'
    n = 2  # Grau do polinômio de Newton-Cotes
    m = 6  # Número de subintervalos

    @staticmethod
    def f(x):
        # Função estática que retorna o seno de x
        return math.sin(x)

# Coeficientes para a fórmula de Newton-Cotes
d = [2, 6, 8, 90, 288, 840, 17280, 28350]
c = [1, 1, 4, 1, 3, 7, 32, 12, 19, 75, 50, 
     41, 216, 27, 272, 751, 3577, 1323, 2989, 
     989, 5888, -928, 10496, -4540]


def integ_new_c(a, b, n, m, c, d, f):
    # Inicializa a condição de erro e o valor da integral
    cond_erro = 0
    integral = 0

    # Verifica as condições de erro para os parâmetros
    if n < 1 or n > 8:
        cond_erro += 1
    
    if m % n != 0:
        cond_erro += 2

    # Retorna imediatamente se houver erro
    if cond_erro != 0:
        return integral, cond_erro
    
    # Calcula o passo dos subintervalos
    p = int(0.25 * (n * (n + 2)) + n % 2)
    h = (b - a) / m 

    # Executa a regra de Newton-Cotes sobre os subintervalos
    for i in range(m + 1):
        x = a + i * h  # Calcula o ponto atual x
        y = f(x)  # Avalia a função no ponto x
        j = p + int(0.5 * n - abs((i % n) - 0.5 * n))
        k = 1 + int((n - (i % n)) / n) - int((m - (i % m)) / m)
        integral += y * c[j] * k  # Acumula o valor ponderado no integral

        # Mostra os valores intermediários para depuração
        print(i, x, y, c[j], k)
    
    # Calcula o valor final da integral
    integral *= n * h / d[n]
    return integral, cond_erro

# Executa a função de integração e imprime o resultado
integral_result, error_condition = integ_new_c(Dado.a, Dado.b, Dado.n, Dado.m, c, d, Dado.f)
print(f"Integral: {integral_result}, Condition Error: {error_condition}")
