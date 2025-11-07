def fatorial(n):
    """Calcula o fatorial de um número inteiro não negativo (n!)."""
    # Caso Base: Condição de parada
    if n == 0:
        return 1
    # Passo Recursivo: n! = n * (n-1)!
    else:
        return n * fatorial(n - 1)

print("## A. Fatorial (n!)")
for n in range(7): # Teste para 0 a 6
    resultado = fatorial(n)
    print(f"Fatorial de {n}! é: **{resultado}**")