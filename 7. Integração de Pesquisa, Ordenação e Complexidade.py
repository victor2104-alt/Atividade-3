import time
import random
import sys

# Definindo constantes
TAMANHO_LISTA = 1000
VALOR_MIN = 1
VALOR_MAX = 10000
# Aumenta o limite de recursão para garantir que o quicksort funcione
sys.setrecursionlimit(TAMANHO_LISTA + 50) 

# ====================================================================
# A. FUNÇÕES DE ORDENAÇÃO (Otimizadas para medição de tempo)
# ====================================================================

# 1. Ordenação por Seleção (O(N²))
def ordenacao_selecao(lista):
    n = len(lista)
    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        if indice_min != i:
            lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista

# 2. Quicksort (O(N log N) em média)
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

# ====================================================================
# B. FUNÇÕES DE PESQUISA (Com contagem de comparações)
# ====================================================================

# 1. Pesquisa Sequencial (O(N))
def pesquisa_sequencial(lista, valor):
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == valor:
            return i, comparacoes
    return -1, comparacoes

# 2. Pesquisa Binária (O(log N))
def pesquisa_binaria(lista, valor):
    baixo = 0
    alto = len(lista) - 1
    comparacoes = 0
    while baixo <= alto:
        comparacoes += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]
        
        if chute == valor:
            return meio, comparacoes
        elif chute < valor:
            baixo = meio + 1
        else:
            alto = meio - 1
            
    return -1, comparacoes

# ====================================================================
# C. PROGRAMA PRINCIPAL
# ====================================================================

print(f"--- 7. Integração de Pesquisa, Ordenação e Complexidade (N={TAMANHO_LISTA}) ---")

# 1. Geração da Lista Aleatória
lista_original = [random.randint(VALOR_MIN, VALOR_MAX) for _ in range(TAMANHO_LISTA)]

# Preparando cópias para cada método de ordenação
lista_sel = lista_original[:]
lista_quick = lista_original[:]
lista_sorted = lista_original[:]

tempos = {}

# 2. Medição do Tempo de Ordenação

# A. Ordenação por Seleção (O(N²))
inicio = time.perf_counter()
ordenacao_selecao(lista_sel)
fim = time.perf_counter()
tempos['Seleção'] = (fim - inicio) * 1000

# B. Quicksort (O(N log N) em média)
inicio = time.perf_counter()
quicksort(lista_quick)
fim = time.perf_counter()
tempos['Quicksort'] = (fim - inicio) * 1000

# C. Função sorted() do Python (Timsort O(N log N))
inicio = time.perf_counter()
lista_sorted = sorted(lista_sorted)
fim = time.perf_counter()
tempos['sorted() Python'] = (fim - inicio) * 1000

# Exibição dos Tempos de Ordenação
print("\n[A] TEMPO DE EXECUÇÃO DOS ALGORITMOS DE ORDENAÇÃO")
print("-------------------------------------------------------")
print(f"| {'Método':<20} | {'Complexidade':<15} | {'Tempo (ms)':>15} |")
print("|----------------------|-----------------|-----------------|")
for metodo, tempo in tempos.items():
    complexidade = "O(N²)" if metodo == "Seleção" else "O(N log N)"
    print(f"| {metodo:<20} | {complexidade:<15} | {tempo:>15.4f} |")
print("-------------------------------------------------------")


# 3. Teste de Pesquisa

# Para o teste, usamos a lista ordenada pelo Quicksort
lista_para_busca = lista_quick
# Valor presente na lista (simulando um valor que será encontrado)
VALOR_PRESENTE = lista_para_busca[random.randint(0, TAMANHO_LISTA - 1)]
# Valor ausente na lista (fora do range)
VALOR_AUSENTE = VALOR_MAX + 100

print("\n[B] COMPARAÇÃO DO NÚMERO DE COMPARAÇÕES NA BUSCA")
print(f"Lista de tamanho N={TAMANHO_LISTA}")
print("------------------------------------------------------------------")

# Teste 1: Buscar um valor presente (o melhor cenário para Sequencial)
print(f"\nTeste 1: Valor Presente (Exemplo: {VALOR_PRESENTE})")
_, comps_seq_pres = pesquisa_sequencial(lista_para_busca, VALOR_PRESENTE)
_, comps_bin_pres = pesquisa_binaria(lista_para_busca, VALOR_PRESENTE)

print(f"  - Pesquisa Sequencial (O(N)): {comps_seq_pres} comparações")
print(f"  - Pesquisa Binária (O(log N)): {comps_bin_pres} comparações")

# Teste 2: Buscar um valor ausente (o pior cenário para ambos)
print(f"\nTeste 2: Valor Ausente (Exemplo: {VALOR_AUSENTE})")
_, comps_seq_aus = pesquisa_sequencial(lista_para_busca, VALOR_AUSENTE)
_, comps_bin_aus = pesquisa_binaria(lista_para_busca, VALOR_AUSENTE)

print(f"  - Pesquisa Sequencial (O(N)): {comps_seq_aus} comparações (N)")
print(f"  - Pesquisa Binária (O(log N)): {comps_bin_aus} comparações (~log₂N)")

print("------------------------------------------------------------------")
print("\n**Conclusão da Busca:** Para listas grandes, a Pesquisa Binária é drasticamente superior, fazendo uma fração mínima das comparações.")