"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from estrutura_sequencial import ex_17
    >>> ex_17.input = lambda k: '100'
    >>> ex_17.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105.
    Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17.input = lambda k: '200'
    >>> ex_17.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185.
    Vão sobrar 2.6 litro(s) de tinta.

"""
import math


def calcular_latas_e_preco_de_tinta():
    lata_litros = 18
    galao_litros = 3.6
    preco_lata = 80
    preco_galao = 25
    cobertura_litro_area = 6

    area = (float(input('Qual a área a ser pintada (m²)? \n'))) * 1.1
    litros = math.ceil(area / cobertura_litro_area)

    # somente latas
    latas = math.ceil(litros / lata_litros)
    preco_latas = latas * preco_lata
    litros_latas = latas * lata_litros
    litros_restantes_latas = litros_latas - litros

    # somente galões
    galoes = math.ceil(litros / galao_litros)
    preco_galoes = galoes * preco_galao
    litros_galoes = galoes * galao_litros
    litros_restantes_galoes = litros_galoes - litros

    print(f'Você deve comprar {litros:.0f} litros de tinta.')
    print(f'Você pode comprar {latas:.0f} lata(s) de 18 litros a um custo de R$ {preco_latas}. Vão sobrar '
          f'{litros_restantes_latas:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {galoes:.0f} lata(s) de 3.6 litros a um custo de R$ {preco_galoes}. Vão sobrar '
          f'{litros_restantes_galoes:.1f} litro(s) de tinta.')

    # Compra otimizada
    latas = math.floor(litros / lata_litros)
    litros_latas = latas * lata_litros
    litros_restantes_latas = litros - litros_latas
    galoes = math.ceil(litros_restantes_latas / galao_litros)
    preco_latas = latas * preco_lata
    preco_galoes = galoes * preco_galao
    preco_total = preco_latas + preco_galoes
    litros_totais = latas * lata_litros + galoes * galao_litros
    litros_restantes = litros_totais - litros

    print(f'Para menor custo, você pode comprar {latas} lata(s) de 18 litros e {galoes} galão(ões) de 3.6 litros a um '
          f'custo de R$ {preco_total}.')
    print(f'Vão sobrar {litros_restantes:.1f} litro(s) de tinta.')


if __name__ == '__main__':
    calcular_latas_e_preco_de_tinta()
