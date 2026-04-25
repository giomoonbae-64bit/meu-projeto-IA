// ...existing code...
Linha 1: from typing import List, Tuple
- Importa as anotações de tipo List e Tuple do módulo typing para uso nas assinaturas e variáveis.

Linha 2:
- Linha em branco para separar visualmente as seções do código.

Linha 3: def is_prime(n: int) -> bool:
- Declara a função is_prime que recebe um inteiro n e retorna um booleano.

Linha 4:     """
- Início da docstring da função para descrever comportamento e parâmetros.

Linha 5:     Verifica se um número é primo.
- Resumo curto do propósito da função.

Linha 6:
- Linha em branco dentro da docstring para melhorar legibilidade.

Linha 7:     Um número primo é maior que 1 e não possui divisores positivos além de 1 e ele mesmo.
- Explica o conceito matemático de número primo usado como referência.

Linha 8:
- Linha em branco na docstring.

Linha 9:     Args:
- Início da seção que descreve os argumentos da função.

Linha 10:         n (int): O número a ser verificado. Deve ser um inteiro.
- Descrição do parâmetro n e seu tipo esperado.

Linha 11:
- Linha em branco na docstring.

Linha 12:     Returns:
- Início da seção que descreve o valor retornado.

Linha 13:         bool: True se o número for primo, False caso contrário.
- Indica que a função devolve um booleano indicando primalidade.

Linha 14:
- Linha em branco na docstring.

Linha 15:     Raises:
- Início da seção que lista exceções que podem ser lançadas.

Linha 16:         TypeError: Se n não for um inteiro.
- Especifica que será levantado TypeError se o argumento não for int.

Linha 17:     """
- Fim da docstring.

Linha 18:     if not isinstance(n, int):
- Verifica se n é do tipo inteiro; protege contra tipos inválidos.

Linha 19:         raise TypeError("O argumento 'n' deve ser um inteiro.")
- Lança TypeError com mensagem clara quando n não é int.

Linha 20:
- Linha em branco para separar validações iniciais da lógica principal.

Linha 21:     # Casos básicos: números <= 1 não são primos
- Comentário explicando a verificação seguinte.

Linha 22:     if n <= 1:
- Condição que trata números 1, 0 e negativos.

Linha 23:         return False
- Retorna False para números que não podem ser primos.

Linha 24:     # 2 e 3 são primos
- Comentário para o caso especial de 2 e 3.

Linha 25:     if n <= 3:
- Se n for 2 ou 3 (ou menor, já filtrado), entra aqui.

Linha 26:         return True
- Retorna True porque 2 e 3 são primos.

Linha 27:     # Eliminar múltiplos de 2 e 3
- Comentário explicando as próximas checagens rápidas.

Linha 28:     if n % 2 == 0 or n % 3 == 0:
- Testa se n é divisível por 2 ou por 3.

Linha 29:         return False
- Se for divisível por 2 ou 3, não é primo; retorna False.

Linha 30:     # Verificar fatores da forma 6k ± 1 até √n
- Explica a otimização: apenas testar candidatos da forma 6k±1 até raiz quadrada.

Linha 31:     divisor_candidate = 5
- Inicializa o candidato a divisor com 5 (primeiro número da forma 6k-1 após 3).

Linha 32:     step_size = 6
- Define passo 6 para pular entre candidatos 6k-1 e 6k+1.

Linha 33:     while divisor_candidate * divisor_candidate <= n:
- Loop que testa divisores até que o quadrado do candidato ultrapasse n (≤ √n).

Linha 34:         if n % divisor_candidate == 0 or n % (divisor_candidate + 2) == 0:
- Testa divisibilidade por divisor_candidate (6k-1) e pelo par complementar +2 (6k+1).

Linha 35:             return False
- Se encontrar um divisor, retorna False imediatamente.

Linha 36:         divisor_candidate += step_size
- Avança para o próximo par candidato (incrementa 6 para manter a forma 6k±1).

Linha 37:     return True
- Se nenhum divisor for encontrado até √n, n é primo; retorna True.

Linha 38:
- Linha em branco separando as definições de função.

Linha 39: def run_tests() -> None:
- Declara a função run_tests que não retorna valor, usada para testes simples.

Linha 40:     """
- Início da docstring da função de teste.

Linha 41:     Executa os testes da função is_prime.
- Descrição curta do que a função faz.

Linha 42:     """
- Fim da docstring.

Linha 43:     test_cases: List[Tuple[int, bool]] = [
- Define uma lista anotada de tuplas (número, resultado esperado) chamada test_cases.

Linha 44:         (2, True),
- Caso de teste: 2 deve ser primo.

Linha 45:         (3, True),
- Caso de teste: 3 deve ser primo.

Linha 46:         (4, False),
- Caso de teste: 4 não é primo.

Linha 47:         (17, True),
- Caso de teste: 17 é primo.

Linha 48:         (18, False),
- Caso de teste: 18 não é primo.

Linha 49:     ]
- Fecha a lista de casos de teste.

Linha 50:     for number, expected_result in test_cases:
- Itera por cada tupla, desestruturando em number e expected_result.

Linha 51:         actual_result = is_prime(number)
- Chama is_prime com o número do caso e guarda o resultado.

Linha 52:         status = "PASSOU" if actual_result == expected_result else "FALHOU"
- Determina se o teste passou comparando resultado atual com o esperado.

Linha 53:         print(f"Teste is_prime({number}): {status} (resultado: {actual_result}, esperado: {expected_result})")
- Exibe no console o resumo do teste com número, status e valores.

Linha 54:
- Linha em branco antes do bloco de execução condicional.

Linha 55: if __name__ == "__main__":
- Verifica se o módulo está sendo executado como script principal.

Linha 56:     run_tests()
- Se sim, executa a função de testes, imprimindo os resultados para o usuário.
