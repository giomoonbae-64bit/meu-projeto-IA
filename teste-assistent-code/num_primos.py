def is_prime(n: int) -> bool:
    """
    Verifica se um número é primo.

    Um número primo é maior que 1 e não possui divisores positivos além de 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
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
    while divisor_candidate * divisor_candidate <= n:
        if n % divisor_candidate == 0 or n % (divisor_candidate + 2) == 0:
            return False
        divisor_candidate += 6
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