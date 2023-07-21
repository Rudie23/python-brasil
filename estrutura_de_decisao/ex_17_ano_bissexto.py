"""
Exercício 17 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto.
    >>> ano_bissexto(100)
    False
    >>> ano_bissexto(400)
    True
    >>> ano_bissexto(800)
    True
    >>> ano_bissexto(2100)
    False
    >>> ano_bissexto(2004)
    True
    >>> ano_bissexto(2022)
    False

"""


def ano_bissexto(ano: int) -> bool:
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
