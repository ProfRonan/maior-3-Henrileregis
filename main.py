"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI

    n1 = float(input("Digite o primeiro número.\n"))
    n2 = float(input("Digite o segundo número.\n"))
    n3 = float(input("Digite o terceiro número.\n"))

    if n1 >= n2 and n1 >= n3:
        maior = n1
    elif n2 >= n1 and n2 >= n3:
        maior = n2
    else:
        maior = n3

    print(f"{maior}")


if __name__ == '__main__':
    main()
