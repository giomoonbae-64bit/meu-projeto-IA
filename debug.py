def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def main() -> None:
    cliente = input("Qual é seu nome? ")

    qtd1 = read_int("Quantidade do item 1: ")
    item1 = read_float("Preço do item 1: ")

    qtd2 = read_int("Quantidade do item 2: ")
    item2 = read_float("Preço do item 2: ")

    qtd3 = read_int("Quantidade do item 3: ")
    item3 = read_float("Preço do item 3: ")

    total_item1 = qtd1 * item1
    total_item2 = qtd2 * item2
    total_item3 = qtd3 * item3

    subtotal = total_item1 + total_item2 + total_item3
    imposto = subtotal * 0.10

    desconto_percentual = read_float(
        "Você tem um cupom de desconto? (Digite o percentual ou 0): "
    )
    desconto = subtotal * (desconto_percentual / 100)

    total = subtotal + imposto - desconto

    linha = "=" * 31
    separador = "-" * 31

    print(linha)
    print(f" Cliente: {cliente}")
    print(linha)
    print(f" Item 1:        R$ {total_item1:.2f}")
    print(f" Item 2:        R$ {total_item2:.2f}")
    print(f" Item 3:        R$ {total_item3:.2f}")
    print(separador)
    print(f" Subtotal:      R$ {subtotal:.2f}")
    print(f" Imposto (10%): R$ {imposto:.2f}")

    if desconto_percentual > 0:
        print(
            f" Desconto ({desconto_percentual:.0f}%): -R$ {desconto:.2f}"
        )

    print(linha)
    print(f" TOTAL:         R$ {total:.2f}")
    print(linha)


if __name__ == "__main__":
    main()