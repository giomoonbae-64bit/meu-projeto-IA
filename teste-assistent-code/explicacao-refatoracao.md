# Explicação da Refatoração

## Melhorias aplicadas no código

### 1. Separação da lógica em função
A verificação de número primo foi isolada na função `is_prime`, facilitando reutilização e organização do código.

### 2. Validação de tipo
Foi adicionada verificação para garantir que o valor recebido seja um número inteiro:

```python
if not isinstance(n, int):
    raise TypeError("O argumento 'n' deve ser um inteiro.")
