"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

    >>> from estrutura_sequencial import ex_16
    >>> ex_16.input = lambda k: '50'
    >>> ex_16.calcular_latas_e_preco_de_tinta()
    Você deve comprar 1 lata(s) tinta ao custo de R$ 80.00
    >>> ex_16.input = lambda k: '100'
    >>> ex_16.calcular_latas_e_preco_de_tinta()
    Você deve comprar 2 lata(s) tinta ao custo de R$ 160.00


"""


def calcular_latas_e_preco_de_tinta():
    cobertura_litro_area = 3
    lata = 18
    preco_lata = 80

    area = float(input('Qual a área a ser pintada? \n'))
    cobertura = area / cobertura_litro_area

    """
    Pra arredondar pra baixo um número num basta fazer:
    round(num - 0.5)

    Para arredondar pra cima:
    round(num + 0.5)
    """

    latas = round(cobertura / lata)
    preco_total = latas * preco_lata
    print(f'Você deve comprar {latas} lata(s) tinta ao custo de R$ {preco_total:.2f}')


if __name__ == '__main__':
    calcular_latas_e_preco_de_tinta()
