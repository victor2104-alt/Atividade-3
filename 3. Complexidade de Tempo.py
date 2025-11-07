import time
import random

# --- Funções de Busca (Revisadas para simplicidade na medição) ---
def pesquisa_sequencial(lista, valor):
    """ Retorna o índice da pesquisa sequencial (sem contagem de comparações) """
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def pesquisa_binaria(lista, valor):
    """ Retorna o índice da pesquisa binária (sem contagem de comparações) """
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == valor:
            return meio
        elif chute < valor:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1

# --- Teste de Execução ---

TAMANHOS = [10_000, 100_000, 1_000_000]
print("--- Teste de Tempo de Execução em Listas Grandes ---")

for N in TAMANHOS:
    # 1. Preparação da Lista
    # Gerar uma lista ordenada (essencial para a Pesquisa Binária)
    lista_grande = list(range(1, N + 1))
    
    # 2. Definir o Valor de Busca (Pior Caso para Sequencial)
    # Buscamos o último elemento da lista
    VALOR_BUSCA = N 
    
    # 3. Medição da Pesquisa Sequencial (O(N))
    inicio_seq = time.perf_counter()
    pesquisa_sequencial(lista_grande, VALOR_BUSCA)
    fim_seq = time.perf_counter()
    tempo_seq = (fim_seq - inicio_seq) * 1000 # Convertido para milissegundos (ms)

    # 4. Medição da Pesquisa Binária (O(log N))
    inicio_bin = time.perf_counter()
    pesquisa_binaria(lista_grande, VALOR_BUSCA)
    fim_bin = time.perf_counter()
    tempo_bin = (fim_bin - inicio_bin) * 1000 # Convertido para milissegundos (ms)

    # 5. Apresentação dos Resultados
    print(f"\n✅ Tamanho da Lista (N): **{N:,}**")
    print(f"   * Seq. (O(N)): {tempo_seq:.6f} ms")
    print(f"   * Bin. (O(log N)): {tempo_bin:.6f} ms")