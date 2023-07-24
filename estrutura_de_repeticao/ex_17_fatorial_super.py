"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

    >>> calcular_fatorial(0)
    1
    >>> calcular_fatorial(1)
    1
    >>> calcular_fatorial(2)
    2 x 1 = 2
    >>> calcular_fatorial(3)
    3 x 2 x 1 = 6
    >>> calcular_fatorial(4)
    4 x 3 x 2 x 1 = 24
    >>> calcular_fatorial(5)
    5 x 4 x 3 x 2 x 1 = 120

"""


def calcular_fatorial(num: int) -> int:
    """Escreva aqui em baixo a sua solução"""
    if num == 1:
        return 1
    fact = 1
    while num > 0:
        print(f'{num}', end='')
        print(' x ' if num > 1 else ' = ', end='')
        fact *= num
        num -= 1

    print(f'{fact}')


if __name__ == '__main__':
    calcular_fatorial(5)
