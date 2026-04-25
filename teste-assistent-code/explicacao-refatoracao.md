# Explicação linha a linha de `refatoracao.py`

Este documento contém uma explicação detalhada, em Português, de cada linha do arquivo `refatoracao.py` recebido.

---

1. from typing import List, Tuple
	- Importa tipos genéricos `List` e `Tuple` do módulo `typing` para usar em anotações de tipo.

2. 
3. def is_prime(n: int) -> bool:
	- Declaração da função `is_prime` que recebe um parâmetro `n` do tipo `int` e retorna um `bool`.

4.     """
5.     Verifica se um número é primo.

6.     Um número primo é maior que 1 e não possui divisores positivos além de 1 e ele mesmo.

7.     Args:
8.         n (int): O número a ser verificado. Deve ser um inteiro.

9.     Returns:
10.         bool: True se o número for primo, False caso contrário.

11.     Raises:
12.         TypeError: Se n não for um inteiro.
13.     """
	- Docstring que explica a finalidade da função, parâmetros, valor de retorno e possíveis exceções.

14.     if not isinstance(n, int):
	- Verifica se o argumento `n` é uma instância de `int`.

15.         raise TypeError("O argumento 'n' deve ser um inteiro.")
	- Se `n` não for um inteiro, lança um `TypeError` com uma mensagem explicativa.

16. 
17.     # Casos básicos: números <= 1 não são primos
	- Comentário explicando que a próxima verificação trata de casos triviais.

18.     if n <= 1:
	- Se `n` for menor ou igual a 1, não é primo.

19.         return False
	- Retorna `False` para números <= 1.

20.     # 2 e 3 são primos
	- Comentário: trata explicitamente os pequenos primos 2 e 3.

21.     if n <= 3:
	- Se `n` for 2 ou 3 (já que valores <=1 foram filtrados), é primo.

22.         return True
	- Retorna `True` para 2 e 3.

23.     # Eliminar múltiplos de 2 e 3
	- Comentário explicando que múltiplos de 2 e 3 serão descartados cedo para eficiência.

24.     if n % 2 == 0 or n % 3 == 0:
	- Se `n` for divisível por 2 ou por 3, não é primo (exceto 2 e 3, já tratados acima).

25.         return False
	- Retorna `False` quando `n` tem divisor 2 ou 3.

26.     # Verificar fatores da forma 6k ± 1 até √n
	- Comentário: utiliza a propriedade que todos os primos além de 3 estão na forma 6k ± 1.

27.     divisor_candidate = 5
	- Inicializa o candidato a divisor em 5 (corresponde a 6*1 - 1).

28.     step_size = 6
	- Define o passo de iteração como 6; será usado para verificar pares 6k-1 e 6k+1.

29.     while divisor_candidate * divisor_candidate <= n:
	- Loop que continua enquanto o quadrado do candidato for <= n. Isso equivale a testar divisores até √n.

30.         if n % divisor_candidate == 0 or n % (divisor_candidate + 2) == 0:
	- Verifica se `n` é divisível por `divisor_candidate` (6k-1) ou por `divisor_candidate + 2` (6k+1).

31.             return False
	- Se `n` for divisível por algum desses candidatos, retorna `False` (não é primo).

32.         divisor_candidate += step_size
	- Avança o `divisor_candidate` em `step_size` (6) para testar o próximo par 6k-1 e 6k+1.

33.     return True
	- Se nenhum divisor foi encontrado até √n, `n` é primo; retorna `True`.

34. 
35. def run_tests() -> None:
	- Declaração de uma função `run_tests` que não retorna valor (-> None). Serve para executar testes simples.

36.     """
37.     Executa os testes da função is_prime.
38.     """
	- Docstring curta explicando que a função roda testes da `is_prime`.

39.     test_cases: List[Tuple[int, bool]] = [
	- Define uma lista anotada `test_cases` contendo tuplas (número, resultado_esperado).

40.         (2, True),
	- Caso de teste: 2 é primo.

41.         (3, True),
	- Caso de teste: 3 é primo.

42.         (4, False),
	- Caso de teste: 4 não é primo.

43.         (17, True),
	- Caso de teste: 17 é primo.

44.         (18, False),
	- Caso de teste: 18 não é primo.

45.     ]
	- Fecha a lista de casos de teste.

46.     for number, expected_result in test_cases:
	- Itera sobre cada tupla de `test_cases`, desempacotando em `number` e `expected_result`.

47.         actual_result = is_prime(number)
	- Chama `is_prime` com o número de teste e armazena o resultado real.

48.         status = "PASSOU" if actual_result == expected_result else "FALHOU"
	- Define `status` como "PASSOU" quando o resultado real bate com o esperado, caso contrário "FALHOU".

49.         print(f"Teste is_prime({number}): {status} (resultado: {actual_result}, esperado: {expected_result})")
	- Imprime uma linha de saída descrevendo o teste, o resultado obtido e o esperado.

50. 
51. if __name__ == "__main__":
	- Verifica se o arquivo está sendo executado como script principal (não importado como módulo).

52.     run_tests()
	- Se for o script principal, chama `run_tests()` para executar os testes rápidos.

---

Observações finais:
- A função `is_prime` está bem escrita e usa otimizações clássicas (remoção de múltiplos de 2/3 e teste na forma 6k ± 1) para reduzir o número de divisões até √n.
- `run_tests` fornece um pequeno conjunto de casos de fumaça (smoke tests) que ajudam a garantir o comportamento esperado para alguns valores comuns.
- Sugestões de melhorias (opcionais): adicionar testes automatizados com `unittest` ou `pytest`, e incluir casos de borda adicionais (0, 1, números negativos, números grandes) se necessário.


