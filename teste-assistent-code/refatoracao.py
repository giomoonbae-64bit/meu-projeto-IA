from typing import List, Tuple

def is_prime(n: int) -> bool:
    """
    Verifica se um número é primo.

    Um número primo é maior que 1 e não possui divisores positivos além de 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado. Deve ser um inteiro.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se n não for um inteiro.
    """
    if not isinstance(n, int):
        raise TypeError("O argumento 'n' deve ser um inteiro.")

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
    step_size = 6
    while divisor_candidate * divisor_candidate <= n:
        if n % divisor_candidate == 0 or n % (divisor_candidate + 2) == 0:
            return False
        divisor_candidate += step_size
    return True

def run_tests() -> None:
    """
    Executa os testes da função is_prime.
    """
    test_cases: List[Tuple[int, bool]] = [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
    ]
    for number, expected_result in test_cases:
        actual_result = is_prime(number)
        status = "PASSOU" if actual_result == expected_result else "FALHOU"
        print(f"Teste is_prime({number}): {status} (resultado: {actual_result}, esperado: {expected_result})")

if __name__ == "__main__":
    run_tests()