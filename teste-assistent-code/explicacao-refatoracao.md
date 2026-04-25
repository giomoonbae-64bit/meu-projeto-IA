Explicação linha por linha
Importações
pythonfrom typing import List, Tuple
Importa os tipos List e Tuple do módulo typing, usados para anotações de tipo nas funções.

Função is_prime(n)
pythondef is_prime(n: int) -> bool:
Define a função is_prime que recebe um inteiro n e retorna um bool.

pythonif not isinstance(n, int):
    raise TypeError("O argumento 'n' deve ser um inteiro.")
Valida se n é realmente um inteiro. Se não for, lança um TypeError.

pythonif n <= 1:
    return False
Números menores ou iguais a 1 não são primos por definição. Retorna False imediatamente.

pythonif n <= 3:
    return True
Os números 2 e 3 são primos. Como já eliminamos os ≤ 1, qualquer valor entre 2 e 3 é primo.

pythonif n % 2 == 0 or n % 3 == 0:
    return False
Elimina de forma rápida todos os múltiplos de 2 e 3 (ex: 4, 6, 9, 12...), que certamente não são primos.

pythondivisor_candidate = 5
step_size = 6
Define o candidato a divisor começando em 5 e um passo de 6. Isso é baseado no fato matemático de que todo primo ≥ 5 está na forma 6k ± 1.

pythonwhile divisor_candidate * divisor_candidate <= n:
Itera enquanto o candidato for menor ou igual a √n. Não é necessário verificar além disso, pois se n tivesse um fator maior que √n, o fator correspondente seria menor que √n e já teria sido encontrado.

python    if n % divisor_candidate == 0 or n % (divisor_candidate + 2) == 0:
        return False
Testa os dois candidatos do par 6k ± 1: divisor_candidate (forma 6k - 1) e divisor_candidate + 2 (forma 6k + 1). Se n for divisível por qualquer um deles, não é primo.

python    divisor_candidate += step_size
Avança o candidato em 6 posições para o próximo par 6k ± 1.

pythonreturn True
Se nenhum divisor foi encontrado, n é primo.

Função run_tests()
pythontest_cases: List[Tuple[int, bool]] = [
    (2, True), (3, True), (4, False), (17, True), (18, False),
]
Define uma lista de tuplas com pares (número, resultado_esperado) para os testes.

pythonfor number, expected_result in test_cases:
    actual_result = is_prime(number)
Percorre cada caso de teste e chama is_prime() com o número.

python    status = "PASSOU" if actual_result == expected_result else "FALHOU"
    print(f"Teste is_prime({number}): {status} ...")
Compara o resultado real com o esperado e imprime se o teste passou ou falhou.

Bloco principal
pythonif __name__ == "__main__":
    run_tests()
Garante que run_tests() só seja executado quando o arquivo for rodado diretamente, e não quando importado como módulo.
