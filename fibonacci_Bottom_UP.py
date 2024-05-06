def fibonacci_bottom_up(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Utwórz tablicę wyników do przechowywania obliczonych wartości Fibonacciego
    fib = [0] * (n + 1)
    fib[1] = 1  # Pierwszy wyraz Fibonacciego (F(1))
    
    # Oblicz kolejne wyrazy ciągu Fibonacciego od F(2) do F(n)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Przykład użycia funkcji fibonacci_bottom_up
n = 519
result = fibonacci_bottom_up(n)
print(f"N-ty wyraz ciagu Fibonacciego dla n = {n} to: {result}")
