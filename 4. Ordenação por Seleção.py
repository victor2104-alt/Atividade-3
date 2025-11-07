import time
import random

def ordenacao_selecao(lista):
    """
    Ordena a lista usando o algoritmo de Ordenação por Seleção,
    exibindo as trocas realizadas.
    """
    n = len(lista)
    trocas = 0
    
    print(f"Lista Inicial: {lista}")
    print("-" * 30)

    # Percorre toda a lista
    for i in range(n - 1):
        # Assume que o elemento atual é o menor
        indice_min = i
        
        # Encontra o menor elemento na sub-lista não ordenada (do índice i+1 até o final)
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        
        # Verifica se o menor elemento encontrado é diferente do elemento atual (i)
        if indice_min != i:
            # Realiza a troca: coloca o menor elemento na posição correta (i)
            valor_trocado = lista[indice_min]
            
            # Troca de posição
            lista[i], lista[indice_min] = lista[indice_min], lista[i]
            trocas += 1
            
            # Mostra o passo a passo da troca
            print(f"Passo {i+1}: Trocando {lista[indice_min]} (índice {indice_min}) por {valor_trocado} (índice {i}).")
            print(f"         Lista Atual: {lista}")

    print("-" * 30)
    print(f"Lista Final Ordenada: {lista}")
    return lista, trocas

# --- Teste de Demonstração Passo a Passo ---

lista_demonstracao = [64, 25, 12, 22, 11]
print("## Demonstração da Ordenação por Seleção (Selection Sort)")
ordenacao_selecao(lista_demonstracao)

# --- Comparação de Tempo de Execução ---

print("\n## Comparação de Tempo com sorted() do Python")
TAMANHO_LISTA = 1000

# 1. Preparação da Lista Não Ordenada
lista_nao_ordenada = [random.randint(1, 10000) for _ in range(TAMANHO_LISTA)]

# Criar cópias para garantir que ambos os algoritmos recebam a mesma lista não ordenada
lista_sel = lista_nao_ordenada[:]
lista_py = lista_nao_ordenada[:]

# --- A. Medição da Ordenação por Seleção (O(N^2)) ---
# Desativamos os prints para a medição de tempo
def ordenacao_selecao_sem_print(lista):
    n = len