# Explicação da Refatoração

## Problemas do código original

- Nomes de variáveis sem significado (c, l, t, mx...)
- Uso desnecessário de range(len(lista))
- Código repetitivo
- Retorno confuso (valores soltos)
- Falta de documentação

## Melhorias aplicadas

### 1. Nomes descritivos
- c → calcular_estatisticas
- l → numeros

### 2. Uso de funções nativas
- sum()
- max()
- min()

### 3. Código mais simples
Remoção de loops desnecessários

### 4. Retorno estruturado
Uso de dicionário ao invés de múltiplos retornos soltos

### 5. Docstring
Adicionada explicação da função

## Resultado

Código mais:
- Legível
- Curto
- Profissional
