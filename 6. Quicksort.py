import time
import random
import sys

# Aumentar o limite de recursão padrão do Python para listas muito grandes.
# Embora 10000 não seja problemático, é uma boa prática para algoritmos recursivos.
sys.setrecursionlimit(2000) 

def quicksort(lista):
    """
    Função principal do Quicksort que chama a função auxiliar recursiva.
    """
    if len(lista) <= 1:
        return lista
    
    # Chama a função recursiva com os índices da lista
    _quicksort_aux(lista, 0, len(lista) - 1)
    return lista

def _quicksort_aux(lista, baixo, alto):
    """
    Função auxiliar recursiva que realiza a ordenação.
    """
    if baixo < alto:
        # Posição do pivô já ordenada (índice de partição)
        pivo_indice = _particao(lista, baixo, alto)
        
        # Chamada recursiva para a sub-lista à esquerda do pivô
        _quicksort_aux(lista, baixo, pivo_indice - 1)
        
        # Chamada recursiva para a sub-lista à direita do pivô
        _quicksort_aux(lista, pivo_indice + 1, alto)

def _particao(lista, baixo, alto):
    """
    Função que escolhe o pivô, move os elementos menores para a esquerda
    e os maiores para a direita, e retorna o índice final do pivô.
    """
    # Escolhe o pivô (usando o último elemento para simplificar)
    pivo = lista[alto]
    
    # Índice do elemento que será trocado com o pivô
    i = baixo - 1
    
    for j in range(baixo, alto):
        # Se o elemento atual for menor ou igual ao pivô
        if lista[j] <= pivo:
            # Move o ponteiro 'i' e troca os elementos
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
            
    # Coloca o pivô em sua posição final correta
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    
    return i + 1

# --- Implementação de Seleção para Comparação (sem print) ---
def ordenacao_selecao(lista):
    """Ordenação por Seleção (O(N^2)) para comparação de tempo."""
    n = len(lista)
    for i in range(n - 1):
        # A variável que guarda o índice mínimo é indice_min
        indice_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        if indice_min != i:
            # CORREÇÃO AQUI: Trocando 'min_idx' por 'indice_min'
            lista[i], lista[indice_min] = lista[indice_min], lista[i] 
    return lista

# --- Teste de Desempenho ---

TAMANHO_LISTA = 10_000
print(f"## Comparação de Desempenho (Lista de {TAMANHO_LISTA:,} elementos)")
print("-" * 60)

# 1. Preparação da Lista Não Ordenada
lista_nao_ordenada = [random.randint(1, TAMANHO_LISTA * 10) for _ in range(TAMANHO_LISTA)]

# Criar cópias
lista_quick = lista_nao_ordenada[:]
lista_sel = lista_nao_ordenada[:]

# --- A. Quicksort (O(N log N) em média) ---
inicio_quick = time.perf_counter()
quicksort(lista_quick)
fim_quick = time.perf_counter()
tempo_quick = (fim_quick - inicio_quick) * 1000 # em milissegundos (ms)

print(f"1. Tempo Quicksort (O(N log N)): **{tempo_quick:.4f} ms**")

# --- B. Ordenação por Seleção (O(N^2)) ---
inicio_sel = time.perf_counter()
ordenacao_selecao(lista_sel)
fim_sel = time.perf_counter()
tempo_sel = (fim_sel - inicio_sel) * 1000 # em milissegundos (ms)

print(f"2. Tempo Seleção (O(N²)): **{tempo_sel:.4f} ms**")

print("-" * 60)