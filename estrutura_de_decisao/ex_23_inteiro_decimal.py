"""
Exercício 23 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.

    >>> inteiro_decimal('256')
    'Inteiro'
    >>> inteiro_decimal('1.0')
    'Inteiro'
    >>> inteiro_decimal('2.0000')
    'Inteiro'
    >>> inteiro_decimal('2.00001')
    'Decimal'
    >>> inteiro_decimal('11.2')
    'Decimal'
    >>> inteiro_decimal('3.1415')
    'Decimal'
"""
from json import loads


def inteiro_decimal(valor: str) -> str:
    valor_numerico = loads(valor)
    valor_round = round(valor_numerico)
    if valor_numerico

    return valor_round


if __name__ == '__main__':
    print(inteiro_decimal('1.00001'))
