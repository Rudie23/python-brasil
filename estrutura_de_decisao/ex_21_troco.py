"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    cem, resto_cem = divmod(valor, 100)
    cinq, resto_cinq = divmod(resto_cem, 50)
    dez, resto_dez = divmod(resto_cinq, 10)
    cinco, um = divmod(resto_dez, 5)

    if valor > 100:
        if cinq and dez and cinco and um:
            return f'{cem} notas de R$ 100, {cinq} nota de R$ 50, {dez} notas de R$ 10, {cinco} nota de R$ 5 e {um} notas de R$ 1'
        if cinq and dez == 0 and um:
            return f'{cem} notas de R$ 100, {cinq} nota de R$ 50, {cinco} nota de R$ 5 e {um} nota de R$ 1'

    if cem == 0:
        if cinq == 0 and dez and cinco == 0 and um:
            return f'{dez} nota de R$ 10 e {um} nota de R$ 1'

    if cinco:
        return f'{cinco} nota de R$ 5'

    if dez:
        return f'{dez} nota de R$ 10'

    if um:
        return f'{um} nota de R$ 1'


if __name__ == '__main__':
    calcular_troco(50)
