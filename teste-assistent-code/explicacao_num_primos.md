# Explicação Técnica da Função `is_prime` em Python

## Visão Geral

A função `is_prime(n)` é implementada em Python para determinar se um número inteiro `n` é primo. Um número primo é definido como um inteiro maior que 1 que não possui divisores positivos além de 1 e ele mesmo.

## Algoritmo Utilizado

O algoritmo empregado é uma versão otimizada do teste de primalidade por tentativa de divisão. Ele evita verificar todos os números até `n-1`, reduzindo a complexidade para O(√n) no pior caso, o que é eficiente para números grandes.

### Passos do Algoritmo:

1. **Verificação de Casos Básicos**:
   - Se `n <= 1`, retorna `False`, pois números menores ou iguais a 1 não são primos.
   - Se `n <= 3`, retorna `True`, pois 2 e 3 são primos.

2. **Verificação de Divisibilidade por 2 e 3**:
   - Se `n` for par (divisível por 2) ou divisível por 3, retorna `False`.

3. **Loop de Verificação**:
   - Inicia com `divisor_candidate = 5`.
   - Enquanto `divisor_candidate * divisor_candidate <= n` (ou seja, `divisor_candidate <= √n`):
     - Verifica se `n` é divisível por `divisor_candidate` ou por `divisor_candidate + 2` (que são os números da forma 6k±1).
     - Se sim, retorna `False`.
     - Incrementa `divisor_candidate` em 6 para pular para o próximo candidato (6k+1 e 6k+5).
   - Se nenhum divisor for encontrado, retorna `True`.

### Otimizações:

- **Eliminação de Pares e Múltiplos de 3**: Reduz as verificações em ~2/3, pois apenas números ímpares e não múltiplos de 3 são testados.
- **Limite até √n**: Suficiente, pois se um número tem um divisor maior que √n, o outro será menor.
- **Incremento de 6**: Aproveita que primos maiores que 3 são da forma 6k±1.

## Código Fonte

```python
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
```

## Casos de Teste

O bloco `if __name__ == "__main__":` executa testes estruturados usando uma lista de tuplas `(número, resultado_esperado)`:
- Para cada caso, imprime o resultado e compara com o esperado, facilitando a validação.

## Complexidade

- **Tempo**: O(√n), devido ao loop até √n.
- **Espaço**: O(1), pois usa apenas variáveis locais.

## Princípios de Clean Code Aplicados

Para melhorar a legibilidade e manutenibilidade do código, aplicamos os seguintes princípios:

- **Nomes Significativos**: A variável `i` foi renomeada para `divisor_candidate` para tornar o propósito claro.
- **Type Hints**: Adicionados `n: int` e `-> bool` para indicar tipos, melhorando a documentação e detecção de erros.
- **Docstring Detalhada**: Expandida para explicar o conceito de primo e descrever argumentos e retorno.
- **Comentários Explicativos**: Adicionados comentários inline para explicar seções do código, sem sobrecarregar.
- **Estrutura de Testes**: Os testes foram organizados em uma lista, tornando-os mais fáceis de expandir e manter.

## Limitações

- Funciona apenas para inteiros. Entradas não inteiras podem causar erros.
- Para números muito grandes, algoritmos probabilísticos como Miller-Rabin são mais eficientes, mas este é determinístico e correto.

Esta implementação é eficiente, limpa e adequada para a maioria dos casos práticos em Python.
