"""
Exercício 22 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo
(resto da divisão).

    >>> par_impar(256)
    'Par'
    >>> par_impar(1)
    'Impar'
    >>> par_impar(5)
    'Impar'
    >>> par_impar(10)
    'Par'
    >>> par_impar(11)
    'Impar'
    >>> par_impar(399)
    'Impar'
"""


def par_impar(valor: int) -> str:
    """Escreva seu código aqui"""
    par = 'Par'
    impar = 'Impar'
    if valor % 2 == 0:
        return par
    else:
        return impar
