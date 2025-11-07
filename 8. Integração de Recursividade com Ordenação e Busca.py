import random
import sys

# Definindo constantes
TAMANHO_LISTA = 20
VALOR_MIN = 1
VALOR_MAX = 50

# Aumenta o limite de recursão para garantir o quicksort
sys.setrecursionlimit(TAMANHO_LISTA + 50) 

# ====================================================================
# A. FUNÇÕES RECURSIVAS
# ====================================================================

# 1. Soma Acumulada Recursiva de Elementos de uma Lista
def soma_acumulada_lista_recursiva(lista):
    """
    Soma acumulada dos elementos de uma lista.
    Complexidade: O(N)
    """
    # Caso Base: Lista vazia
    if not lista:
        return 0
    # Passo Recursivo: elemento atual + soma do restante da lista
    return lista[0] + soma_acumulada_lista_recursiva(lista[1:])

# 2. Quicksort Recursivo (Implementação de Partição e Auxiliar)
# Usaremos a mesma implementação O(N log N) em média do Quicksort da questão 6

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    _quicksort_aux(lista, 0, len(lista) - 1)
    return lista

def _quicksort_aux(lista, baixo, alto):
    if baixo < alto:
        pivo_indice = _particao(lista, baixo, alto)
        _quicksort_aux(lista, baixo, pivo_indice - 1)
        _quicksort_aux(lista, pivo_indice + 1, alto)

def _particao(lista, baixo, alto):
    pivo = lista[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    return i + 1

# 3. Pesquisa Binária Recursiva (O(log N))
def pesquisa_binaria_recursiva(lista, valor, baixo, alto, comparacoes=0):
    """
    Pesquisa Binária recursiva em lista ordenada.
    Retorna (índice, comparações)
    Complexidade: O(log N)
    """
    if baixo > alto:
        # Caso Base 1: Elemento não encontrado
        return -1, comparacoes

    comparacoes += 1
    meio = (baixo + alto) // 2
    
    if lista[meio] == valor:
        # Caso Base 2: Elemento encontrado
        return meio, comparacoes
    elif lista[meio] < valor:
        # Passo Recursivo: Busca na metade superior
        return pesquisa_binaria_recursiva(lista, valor, meio + 1, alto, comparacoes)
    else:
        # Passo Recursivo: Busca na metade inferior
        return pesquisa_binaria_recursiva(lista, valor, baixo, meio - 1, comparacoes)

# 4. Fatorial Recursivo (O(N))
def fatorial(n):
    """
    Calcula o fatorial (n!).
    Complexidade: O(N)
    """
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# 5. Fibonacci Recursivo (O(2^N))
def fibonacci(n):
    """
    Retorna o n-ésimo termo de Fibonacci.
    Complexidade: O(2^N)
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# ====================================================================
# B. FLUXO PRINCIPAL
# ====================================================================

print("--- 8. Integração de Recursividade ---")

# 1. Geração da Lista Aleatória
lista_aleatoria = [random.randint(VALOR_MIN, VALOR_MAX) for _ in range(TAMANHO_LISTA)]
print(f"1. Lista Inicial (N={TAMANHO_LISTA}): {lista_aleatoria}")
print("-" * 50)

# 2. Ordenação com Quicksort (Recursivo)
lista_ordenada = quicksort(lista_aleatoria[:]) # Copia para ordenar
print("2. Lista Ordenada (Quicksort):")
print(lista_ordenada)
print("-" * 50)

# 3. Pesquisa Binária Recursiva
VALOR_BUSCA = 100
indice, comps = pesquisa_binaria_recursiva(lista_ordenada, VALOR_BUSCA, 0, len(lista_ordenada) - 1)

status = "encontrado" if indice != -1 else "NÃO encontrado"
print(f"3. Pesquisa Binária Recursiva (Valor {VALOR_BUSCA}):")
print(f"   Resultado: Valor {status} (Índice: {indice})")
print(f"   Comparações: {comps}")
print("-" * 50)

# 4. Cálculos Adicionais Recursivos

# A. Soma Acumulada da Lista
soma = soma_acumulada_lista_recursiva(lista_ordenada)
print(f"4. A. Soma Acumulada Recursiva dos Elementos da Lista: **{soma}**")

# B. Fatorial do Maior Número
maior_numero = lista_ordenada[-1]
# O fatorial cresce muito rápido, vamos limitar para um resultado prático
fatorial_resultado = fatorial(min(maior_numero, 12)) 
print(f"4. B. Fatorial do Maior Número ({maior_numero}!): **{fatorial_resultado}** (Limitado a 12! para evitar overflow/tempo)")

# C. Fibonacci (n = Tamanho da Lista)
fibonacci_resultado = fibonacci(TAMANHO_LISTA)
print(f"4. C. F_{TAMANHO_LISTA} (Fibonacci de N={TAMANHO_LISTA}): **{fibonacci_resultado}**")

print("-" * 50)

# ====================================================================
# C. ANÁLISE DE COMPLEXIDADE
# ====================================================================

print("## ANÁLISE DE COMPLEXIDADE")
print("-" * 50)

analise_complexidade = [
    ("Soma Recursiva de Lista", "$O(N)$", "Cada chamada processa 1 elemento e avança para o restante $N-1$."),
    ("Quicksort", "$O(N \log N)$ média, $O(N^2)$ pior caso", "Divide o problema em $\log N$ níveis, com $O(N)$ trabalho em cada nível."),
    ("Pesquisa Binária Recursiva", "$O(\log N)$", "Descarta metade da lista a cada chamada recursiva."),
    ("Fatorial", "$O(N)$", "O número de chamadas recursivas é proporcional ao valor de $N$."),
    ("Fibonacci Recursivo", "$O(2^N)$", "Cria uma árvore de chamadas exponencial, recalculando valores várias vezes."),
]

print(f"| {'Função':<30} | {'Complexidade':<25} | {'Justificativa':<60} |")
print("|" + "=" * 120 + "|")
for funcao, complexidade, justificativa in analise_complexidade:
    print(f"| {funcao:<30} | {complexidade:<25} | {justificativa:<60} |")
print("-" * 122)