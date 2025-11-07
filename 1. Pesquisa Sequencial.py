def pesquisa_sequencial(lista, valor):
    """
    Realiza a pesquisa sequencial em uma lista.

    Args:
        lista (list): A lista onde a pesquisa será realizada.
        valor: O valor a ser buscado na lista.

    Returns:
        tuple: Uma tupla contendo (índice_encontrado, comparacoes_realizadas).
               O índice_encontrado será -1 se o valor não for encontrado.
    """
    comparacoes = 0
    
    # 1. Itera sobre a lista, do primeiro ao último elemento
    for i in range(len(lista)):
        # Incrementa o contador de comparações
        comparacoes += 1
        
        # 2. Compara o elemento atual da lista com o valor procurado
        if lista[i] == valor:
            # 3. Valor encontrado: retorna o índice e o total de comparações
            return i, comparacoes
            
    # 4. Loop concluído e valor não encontrado: retorna -1 e o total de comparações
    #    Neste caso, o número de comparações é igual ao tamanho da lista (len(lista)).
    return -1, comparacoes

# --- Teste da Função ---

# Lista de 10 números inteiros para o teste
lista_teste = [42, 15, 88, 7, 23, 91, 5, 60, 34, 19]
print(f"Lista de Teste: {lista_teste}")
print("-" * 30)

# Valores a serem buscados:
valores_a_buscar = [
    7,    # Valor presente (início da lista)
    19,   # Valor presente (final da lista)
    55,   # Valor não presente
    91    # Valor presente (meio da lista)
]

for valor in valores_a_buscar:
    indice, comps = pesquisa_sequencial(lista_teste, valor)
    
    if indice != -1:
        print(f"✅ Valor {valor} encontrado no índice: **{indice}**")
        print(f"   Comparações realizadas: **{comps}**")
    else:
        print(f"❌ Valor {valor} não encontrado (índice: {indice})")
        print(f"   Comparações realizadas: **{comps}** (Tamanho da lista)")