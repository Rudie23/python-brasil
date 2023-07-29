"""
Exercício 21 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é
divisível somente por ele mesmo e por 1.

    >>> primo(0)
    False
    >>> primo(1)
    False
    >>> primo(2)
    True
    >>> primo(3)
    True
    >>> primo(4)
    False
    >>> primo(5)
    True
    >>> primo(6)
    False
    >>> primo(7)
    True
    >>> primo(8)
    False
    >>> primo(9)
    False
    >>> primo(10)
    False
    >>> primo(11)
    True
    >>> primo(547)
    True
    >>> primo(548)
    False

"""


def primo(num: int) -> bool:
    """Escreva aqui em baixo a sua solução"""
    # Program to check if a number is prime or not

    # define a flag variable
    flag = False

    if num == 1 or num == 0:
        return flag
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            return False
        else:
            return True
