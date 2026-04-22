# Explicação do Debug do Código

## Erros identificados

1. `float(input(Preço do item 1? ))`
   - O texto do prompt não estava entre aspas. Isso causa erro de sintaxe, porque o Python interpreta `Preço` como uma variável não definida.

2. `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
   - A entrada do usuário é uma string. Em seguida, o código tenta usar `desconto_cupom / 100`, o que causa um erro de tipo.

3. `if desconto_cupom > 0:`
   - A comparação era feita entre string e número inteiro, o que não é permitido.
   - Além disso, a linha seguinte `print(...)` estava sem indentação correta dentro do bloco `if`, o que gera erro de identação.

4. `print(" Item 2:        R$ {total_item2:.2f}")`
   - A string não era uma f-string. O valor de `total_item2` não era interpolado e o texto era impresso literalmente.

## Correções aplicadas

- Corrigi o prompt de entrada com aspas corretamente.
- Converti a entrada do cupom para `float` antes de usar em cálculos.
- Ajustei a condição `if` para comparar números e adicionei indentação correta.
- Usei f-strings consistentes para todos os prints.
- Estruturei o código em função `main()` para melhorar legibilidade e manutenção.
- Adicionei funções auxiliares para leitura segura de inteiros e reais.

## Resultado

O código agora calcula o total corretamente, aplica imposto e desconto, e formata a saída de forma clara.
