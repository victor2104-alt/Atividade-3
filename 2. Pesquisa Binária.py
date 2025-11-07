import time

def pesquisa_sequencial(lista, valor):
    """
    Pesquisa Sequencial: retorna (índice, comparações)
    (Reutilizando a função anterior para comparação)
    """
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == valor:
            return i, comparacoes
    return -1, comparacoes

def pesquisa_binaria(lista, valor):
    """
    Pesquisa Binária em lista ordenada: retorna (índice, comparações)
    """
    baixo = 0
    alto = len(lista) - 1
    comparacoes = 0
    
    while baixo <= alto:
        comparacoes += 1  # Conta a comparação principal (lista[meio] == valor)
        meio = (baixo + alto) // 2
        
        chute = lista[meio]
        
        if chute == valor:
            # Valor encontrado
            return meio, comparacoes
        elif chute < valor:
            # O valor está na metade superior
            baixo = meio + 1
        else:
            # O valor está na metade inferior
            alto = meio - 1
            
    # Valor não encontrado
    return -1, comparacoes

# --- Geração da Lista de Teste ---

# Lista de 100 números ordenados (range(1, 101))
TAMANHO_LISTA = 100
lista_ordenada = list(range(1, TAMANHO_LISTA + 1))
VALOR_BUSCA = 100  # Valor a ser buscado (Pior Caso para Sequencial)

print(f"Lista gerada: [1, 2, ..., {TAMANHO_LISTA}]")
print(f"Valor buscado: {VALOR_BUSCA}")
print("-" * 50)

# --- A. Comparação de Contagem de Comparações ---

print("## A. Contagem de Comparações")
print("-" * 50)

# 1. Pesquisa Sequencial
indice_seq, comps_seq = pesquisa_sequencial(lista_ordenada, VALOR_BUSCA)
print(f"Pesquisa Sequencial para {VALOR_BUSCA}:")
print(f"  Índice: {indice_seq} | Comparações: **{comps_seq}**")

# 2. Pesquisa Binária
indice_bin, comps_bin = pesquisa_binaria(lista_ordenada, VALOR_BUSCA)
print(f"\nPesquisa Binária para {VALOR_BUSCA}:")
print(f"  Índice: {indice_bin} | Comparações: **{comps_bin}**")

print("\n**Resultado:** A Pesquisa Binária (log2(100) ≈ 6.64) é muito mais eficiente em termos de comparações.")

print("-" * 50)

# --- B. Comparação do Tempo de Execução ---

print("## B. Tempo de Execução")
print(f"(A diferença será mais perceptível em listas muito maiores)")
print("-" * 50)

# Número de repetições para obter um tempo mensurável
REPETICOES = 100000

# 1. Pesquisa Sequencial - Medição de Tempo
inicio = time.perf_counter()
for _ in range(REPETICOES):
    pesquisa_sequencial(lista_ordenada, VALOR_BUSCA)
fim = time.perf_counter()
tempo_seq = (fim - inicio) * 1000

print(f"Pesquisa Sequencial ({REPETICOES} execuções): **{tempo_seq:.4f} ms**")

# 2. Pesquisa Binária - Medição de Tempo
inicio = time.perf_counter()
for _ in range(REPETICOES):
    pesquisa_binaria(lista_ordenada, VALOR_BUSCA)
fim = time.perf_counter()
tempo_bin = (fim - inicio) * 1000

print(f"Pesquisa Binária ({REPETICOES} execuções): **{tempo_bin:.4f} ms**")