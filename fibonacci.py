from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Wywołanie funkcji fibonacci
result = fibonacci(10)
print(result)  # Wynik: 55

# Ponowne wywołanie tej samej funkcji
# Wynik zostanie pobrany z pamięci podręcznej, nie będzie ponownie obliczany
result_again = fibonacci(10)
print(result_again)  # Wynik: 55
