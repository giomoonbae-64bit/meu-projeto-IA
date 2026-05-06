def is_prime(n: int) -> bool:
    """
    Verifica se um número é primo.

    Esta função determina se um número inteiro dado é um número primo, ou seja,
    um número maior que 1 que não possui divisores positivos além de 1 e ele mesmo.
    A implementação utiliza uma otimização baseada na verificação de divisores até
    a raiz quadrada do número, pulando múltiplos de 2 e 3.

    Args:
        n (int): O número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Exemplos:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
    """
    # Casos básicos: números <= 1 não são primos
    if n <= 1:
        return False
    # 2 e 3 são primos
    if n <= 3:
        return True
    # Eliminar múltiplos de 2 e 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Verificar fatores da forma 6k ± 1 até √n
    divisor_candidate = 5
    while divisor_candidate * divisor_candidate <= n:  # Verifica até a raiz quadrada para eficiência
        if n % divisor_candidate == 0 or n % (divisor_candidate + 2) == 0:  # Verifica 6k-1 e 6k+1
            return False
        divisor_candidate += 6  # Próximo par: 6(k+1)±1
    return True

# Testes
if __name__ == "__main__":
    test_cases = [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
    ]
    for num, expected in test_cases:
        result = is_prime(num)
        print(f"is_prime({num}) = {result} (esperado: {expected})")
