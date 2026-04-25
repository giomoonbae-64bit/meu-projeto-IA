from typing import List, Tuple


# ─── Definição da função ─────────────────────────────────────────────────────
# is_prime recebe um inteiro n e retorna True se for primo, False caso contrário.
def is_prime(n: int) -> bool:
    """
    Verifica se um número é primo.
    Um número primo é maior que 1 e não possui divisores
    positivos além de 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado.
    Returns:
        bool: True se primo, False caso contrário.
    Raises:
        TypeError: Se n não for um inteiro.
    """

    # Validação de tipo: se n não for int, lança TypeError imediatamente.
    if not isinstance(n, int):
        raise TypeError("O argumento 'n' deve ser um inteiro.")

    # Caso base 1: qualquer número <= 1 não é primo por definição.
    if n <= 1:
        return False

    # Caso base 2: 2 e 3 são os primeiros primos; retorna True diretamente.
    if n <= 3:
        return True

    # Otimização: elimina múltiplos de 2 e 3 sem entrar no loop.
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Todo primo >= 5 tem a forma 6k-1 ou 6k+1.
    # Começamos em 5 (= 6*1 - 1) e avançamos de 6 em 6.
    divisor_candidate = 5
    step_size = 6

    # Só precisamos testar até √n: se n tivesse fator > √n,
    # o fator correspondente seria < √n e já teria sido encontrado.
    while divisor_candidate * divisor_candidate <= n:

        # Testa o par 6k-1 (divisor_candidate) e 6k+1 (divisor_candidate + 2).
        if n % divisor_candidate == 0 or n % (divisor_candidate + 2) == 0:
            return False  # Divisível → não é primo.

        # Avança para o próximo par 6k±1.
        divisor_candidate += step_size

    # Nenhum divisor encontrado → n é primo.
    return True


# ─── Função de testes ────────────────────────────────────────────────────────
# Percorre uma lista de pares (número, resultado esperado) e valida is_prime.
def run_tests() -> None:
    """Executa os testes da função is_prime."""

    # Cada tupla: (número a testar, resultado esperado).
    test_cases: List[Tuple[int, bool]] = [
        (2,  True),    # menor primo
        (3,  True),    # primo ímpar
        (4,  False),   # par não primo
        (17, True),    # primo maior
        (18, False),   # composto
    ]

    # Itera sobre os casos, chama is_prime e compara com o esperado.
    for number, expected_result in test_cases:
        actual_result = is_prime(number)

        # Expressão ternária: "PASSOU" se correto, "FALHOU" se não.
        status = "PASSOU" if actual_result == expected_result else "FALHOU"

        # Imprime o resultado formatado com f-string.
        print(
            f"Teste is_prime({number}): {status} "
            f"(resultado: {actual_result}, esperado: {expected_result})"
        )


# ─── Ponto de entrada ────────────────────────────────────────────────────────
# Garante que run_tests() só execute quando o arquivo é rodado diretamente,
# não quando é importado como módulo por outro script.
if __name__ == "__main__":
    run_tests()
