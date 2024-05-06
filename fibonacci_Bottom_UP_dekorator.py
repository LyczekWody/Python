from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Utwórz listę do przechowywania obliczonych wartości Fibonacciego
    fib = [0] * (n + 1)
    fib[1] = 1  # Pierwszy wyraz Fibonacciego (F(1))
    
    # Oblicz kolejne wyrazy ciągu Fibonacciego od F(2) do F(n)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Przykład użycia funkcji fibonacci_memoized
n = 10
result = fibonacci_memoized(n)
print(f"N-ty wyraz ciągu Fibonacciego dla n = {n} to: {result}")

# Ponowne wywołanie funkcji z tym samym argumentem
# Wynik zostanie pobrany z pamięci podręcznej, nie będzie ponownie obliczany
result_again = fibonacci_memoized(n)
print(f"N-ty wyraz ciągu Fibonacciego dla n = {n} (z pamięci podręcznej): {result_again}")
